"""One-call Colab setup + helpers for working off Drive's flaky mount.

Two-step pattern we use on Colab (Drive shortcut paths are unreliable):

    # Cell 1: inline bootstrap (no package import yet — Drive may disconnect)
    import os, shutil, sys
    from google.colab import drive
    DRIVE_ROOT = '/content/drive/MyDrive/.../Exact_2026_Laplace-s_Red_Devils'
    LOCAL_ROOT = '/content/Exact_2026_Laplace-s_Red_Devils'
    drive.mount('/content/drive')
    if not os.path.exists(LOCAL_ROOT):
        shutil.copytree(DRIVE_ROOT, LOCAL_ROOT,
                        ignore=shutil.ignore_patterns(
                            '.git', '__pycache__', '*.pyc', '.hf_snapshots', 'runs'))
    os.chdir(LOCAL_ROOT)
    sys.path.insert(0, LOCAL_ROOT)

    # Cell 2: from now on we import from the LOCAL copy
    from app.physics_solution.shared.colab.setup import setup_colab
    setup_colab(repo_root=LOCAL_ROOT)

    # ... run pipeline ...

    # Cell N (end of session): persist results back to Drive
    from app.physics_solution.shared.colab.setup import sync_results_to_drive
    sync_results_to_drive(drive_root=DRIVE_ROOT, local_root=LOCAL_ROOT)

`setup_colab` chdirs, loads `.env`, wires HF + LangSmith. Everything else
(model id, batch size, dtype, ...) lives in `config.py`.
"""

from __future__ import annotations

import os
import shutil
import sys
from pathlib import Path

from dotenv import load_dotenv

from app.physics_solution import config


def _load_dotenv_strict(env_path: Path) -> None:
    if not env_path.exists():
        print(f"[colab_setup] no .env at {env_path} — skipping env load", flush=True)
        return
    load_dotenv(env_path, override=False)
    print(f"[colab_setup] loaded {env_path}", flush=True)


def _wire_hf_token() -> str | None:
    """Accept HF_TOKEN or HF_TOKEN_CC (legacy)."""
    tok = os.environ.get("HF_TOKEN") or os.environ.get("HF_TOKEN_CC")
    if not tok:
        # Last resort: Colab Secrets if available.
        try:
            from google.colab import userdata  # type: ignore

            for name in ("HF_TOKEN", "HF_TOKEN_CC"):
                try:
                    v = userdata.get(name)
                    if v:
                        tok = v
                        break
                except Exception:
                    pass
        except Exception:
            pass
    if not tok:
        return None
    # Normalise: every consumer should see HF_TOKEN + HUGGING_FACE_HUB_TOKEN.
    os.environ["HF_TOKEN"] = tok
    os.environ["HUGGING_FACE_HUB_TOKEN"] = tok
    return tok


def _wire_langsmith(project: str) -> bool:
    api = os.environ.get("LANGSMITH_API_KEY")
    if not api:
        try:
            from google.colab import userdata  # type: ignore

            api = userdata.get("LANGSMITH_API_KEY")
        except Exception:
            pass
        if api:
            os.environ["LANGSMITH_API_KEY"] = api
    if not api:
        return False
    os.environ["LANGSMITH_TRACING"] = "true"
    os.environ["LANGCHAIN_TRACING_V2"] = "true"
    os.environ["LANGSMITH_PROJECT"] = project
    os.environ["LANGCHAIN_PROJECT"] = project
    return True


def setup_colab(
    repo_root: str | os.PathLike | None = None,
    *,
    env_filename: str = "app/physics_solution/.env",
    verbose: bool = True,
) -> dict:
    """Run all the boilerplate. Returns a small summary dict for the caller to print."""
    root = Path(repo_root) if repo_root else config.repo_root()
    os.chdir(root)
    if str(root) not in sys.path:
        sys.path.insert(0, str(root))
    os.environ["REPO_ROOT"] = str(root)

    _load_dotenv_strict(root / env_filename)
    hf_ok = _wire_hf_token() is not None
    ls_ok = _wire_langsmith(config.LANGSMITH_PROJECT)

    summary = {
        "cwd": os.getcwd(),
        "hf_token": "OK" if hf_ok else "MISSING",
        "langsmith": "ON" if ls_ok else "OFF",
        "base_model": config.BASE_MODEL_ID,
        "dtype": config.DTYPE,
        "device": config.DEVICE,
        "batch_size": config.BATCH_SIZE,
        "max_new_tokens": config.MAX_NEW_TOKENS,
        "temperature": config.TEMPERATURE,
        "test_file": config.TEST_FILE,
    }
    if verbose:
        for k, v in summary.items():
            print(f"  {k:>16}: {v}")
    return summary


# ============================================================ Drive sync helpers


# Folders we want to keep in version control / on Drive for inspection.
# Everything else (model weights, HF snapshots, runs, pycache) stays on local SSD.
_DEFAULT_SYNC_SUBDIRS: tuple[str, ...] = (
    "app/physics_solution/results",
    "app/physics_solution/versions/v02_fewshot/examples.json",
)


def sync_results_to_drive(
    drive_root: str | os.PathLike,
    local_root: str | os.PathLike,
    subdirs: tuple[str, ...] | list[str] | None = None,
    *,
    overwrite: bool = True,
    verbose: bool = True,
) -> list[str]:
    """Copy `subdirs` from `local_root` back to `drive_root`.

    Drive is the durable store; the Colab VM's `/content/` is wiped at the
    end of the session. Run this once per session before disconnecting so
    you keep the inference JSONs / few-shot pools.

    Returns the list of paths that were actually synced.
    """
    drive = Path(drive_root)
    local = Path(local_root)
    targets = list(subdirs or _DEFAULT_SYNC_SUBDIRS)

    synced: list[str] = []
    for sub in targets:
        src = local / sub
        dst = drive / sub
        if not src.exists():
            if verbose:
                print(f"  [skip] {src} does not exist")
            continue
        dst.parent.mkdir(parents=True, exist_ok=True)
        if src.is_dir():
            if dst.exists():
                if not overwrite:
                    if verbose:
                        print(f"  [skip] {dst} exists (overwrite=False)")
                    continue
                shutil.rmtree(dst)
            shutil.copytree(src, dst)
        else:
            shutil.copy2(src, dst)
        synced.append(str(dst))
        if verbose:
            print(f"  synced  {src}  ->  {dst}")
    return synced


# ============================================================ Fast-kernel installer


def _try_pip_install(args: list[str], verbose: bool = True) -> tuple[bool, str]:
    import subprocess

    r = subprocess.run(
        [sys.executable, "-m", "pip", "install", "-q", *args],
        capture_output=True,
        text=True,
    )
    ok = r.returncode == 0
    if verbose and not ok:
        tail = (r.stderr or r.stdout or "").strip().splitlines()
        msg = tail[-1] if tail else "(no output)"
        print(f"    -> failed: {msg[:200]}")
    return ok, r.stderr + r.stdout


def install_fast_kernels(*, verbose: bool = True) -> dict:
    """Best-effort install of Qwen3.5's fast-attention kernels.

    Two pieces:
    - `flash-linear-attention` — pure-Python (Triton JIT). Installs cleanly.
    - `causal-conv1d` — CUDA C++ extension. Build from source typically fails
      on Colab Py3.12 because the CUDA toolkit/ABI doesn't match the
      pip-installed torch. We try pre-built wheels from the Dao-AILab GitHub
      release page, walking versions × cxx11_abi until one fits.

    If nothing works the model still runs via the torch fallback (~3× slower
    but functionally identical).

    Returns `{"fla": bool, "causal_conv1d": bool}`.
    """
    try:
        import torch  # noqa: WPS433
    except ImportError:
        print("[install_fast_kernels] torch not importable — skipping.")
        return {"fla": False, "causal_conv1d": False}

    py_tag = f"cp{sys.version_info.major}{sys.version_info.minor}"
    torch_short = ".".join(torch.__version__.split("+")[0].split(".")[:2])  # "2.6"
    cuda_v = torch.version.cuda or "12.0"
    if cuda_v.startswith("11"):
        # cu11 wheels are tagged cu118 etc.
        cuda_tag = f"cu{cuda_v.replace('.', '')[:3]}"
    else:
        # cu12 wheels are just tagged cu12 regardless of 12.x minor.
        cuda_tag = f"cu{cuda_v.split('.')[0]}"

    if verbose:
        print(
            f"[install_fast_kernels] env: python={py_tag} torch={torch_short} "
            f"cuda={cuda_v} -> tag {cuda_tag}"
        )

    # 1) flash-linear-attention — easy path.
    print("[install_fast_kernels] flash-linear-attention ...")
    fla_ok, _ = _try_pip_install(["flash-linear-attention"], verbose=verbose)
    print(f"  fla: {'OK' if fla_ok else 'failed'}")

    # 2) causal-conv1d — pre-built wheel only.
    print("[install_fast_kernels] causal-conv1d (pre-built wheels) ...")
    versions = ["1.5.2", "1.5.0.post8", "1.4.0"]
    abis = ["FALSE", "TRUE"]
    cc_ok = False
    for version in versions:
        for abi in abis:
            url = (
                f"https://github.com/Dao-AILab/causal-conv1d/releases/download/"
                f"v{version}/causal_conv1d-{version}+{cuda_tag}torch{torch_short}"
                f"cxx11abi{abi}-{py_tag}-{py_tag}-linux_x86_64.whl"
            )
            if verbose:
                print(f"  trying v{version} abi={abi} ...")
            cc_ok, _ = _try_pip_install([url], verbose=False)
            if cc_ok:
                print(f"  causal-conv1d: OK ({version}, abi={abi})")
                break
        if cc_ok:
            break
    if not cc_ok:
        print(
            "  causal-conv1d: no pre-built wheel matched this env. "
            "Model will run via torch fallback (slower, but works)."
        )

    return {"fla": fla_ok, "causal_conv1d": cc_ok}


def bootstrap_local(
    drive_root: str | os.PathLike,
    local_root: str | os.PathLike,
    *,
    force_refresh: bool = False,
    verbose: bool = True,
) -> str:
    """Programmatic version of the inline bootstrap snippet.

    Use this when you already have `app.physics_solution.colab_setup`
    importable (e.g. you ran the inline snippet once and want to re-use
    the same logic for re-copies). For the very first cell of a fresh
    Colab runtime, keep the snippet inline — it must not depend on the
    package being on sys.path.

    Returns the local root as a string (suitable for `os.chdir`).
    """
    drive_path = Path(drive_root)
    local_path = Path(local_root)

    try:
        from google.colab import drive as _gdrive  # type: ignore

        _gdrive.mount("/content/drive", force_remount=False)
    except Exception as e:
        if verbose:
            print(f"[bootstrap_local] drive.mount skipped/failed: {e}")

    if force_refresh and local_path.exists():
        if verbose:
            print(f"[bootstrap_local] force_refresh -> removing {local_path}")
        shutil.rmtree(local_path)

    if not local_path.exists():
        if verbose:
            print(f"[bootstrap_local] copying {drive_path} -> {local_path}")
        shutil.copytree(
            drive_path,
            local_path,
            ignore=shutil.ignore_patterns(
                ".git",
                "__pycache__",
                "*.pyc",
                ".hf_snapshots",
                "runs",
                "checkpoints",
                ".ipynb_checkpoints",
            ),
        )
    elif verbose:
        print(
            f"[bootstrap_local] {local_path} already exists — using cached copy "
            "(set force_refresh=True to re-copy from Drive)"
        )

    os.chdir(local_path)
    if str(local_path) not in sys.path:
        sys.path.insert(0, str(local_path))
    return str(local_path)
