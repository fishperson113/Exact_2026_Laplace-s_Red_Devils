"""v05_best_vLLM is served via API — use eval_api.py for batch evaluation."""


def run(args) -> None:  # noqa: ARG001
    raise SystemExit(
        "\nv05_best_vLLM requires the vLLM API server.\n"
        "Start the server on Vast AI (see README_GPU_SETUP.md), then run:\n\n"
        "  python -m app.physics_solution.cli.eval_api \\\n"
        "      --api-url https://<tunnel>.trycloudflare.com \\\n"
        "      --concurrency 1\n"
    )
