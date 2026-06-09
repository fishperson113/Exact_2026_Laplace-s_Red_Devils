"""z3_playground.py — Bàn thử khả năng SOLVE của Z3 trên FOL.

Mục đích: nạp 1 bài (question + premises FOL) ở dạng JSON, xem Z3:
  1. parse từng premise FOL ra sao (OK / FAIL + biểu thức Z3),
  2. tập premises có nhất quán không (consistency),
  3. suy ra đáp án thế nào (entailment),
  4. ⭐ DÙNG ĐÚNG NHỮNG PREMISE NÀO để giải — qua **unsat core**
     (= premises_used provable, không phải LLM tự khai).

Harness này IMPORT thẳng parser/translator THẬT của pipeline
(evaluation.fol_parser + evaluation.fol_z3_translator) nên những gì bạn
thấy ở đây đúng bằng khả năng solve thật của hệ thống.

──────────────────────────────────────────────────────────────────────────────
CÁCH DÙNG
    python z3_playground.py            # ví dụ pure-FOL (không cần model)
    python z3_playground.py nl         # ví dụ NL → model FOL tự dịch sang FOL
    python z3_playground.py case.json  # bài của bạn

JSON đầu vào (1 object, hoặc 1 list nhiều object):
{
  "type": "yesno",                  // "yesno" | "mcq"
  "question": "câu hỏi NL",
  "premises_fol": ["∀x (...)", "..."],   // 0-indexed (premises luôn ở dạng FOL)
  "question_fol": "∀x (...)",        // yesno: nếu THIẾU → model dịch từ "question"
  "options":     {"A": "text NL"},   // mcq: options dạng NL → model dịch
  "options_fol": {"A": "∀x (...)"}   // mcq: hoặc đưa thẳng FOL (khỏi cần model)
}
Quy tắc: có *_fol thì dùng thẳng; THIẾU thì model FOL tự dịch từ question/options.
Ký hiệu chấp nhận cả Unicode (∀ ∃ → ∧ ∨ ¬ ↔ ≥ ≤ ≠) lẫn ASCII (forall, ->, >=, !=, and, or).
──────────────────────────────────────────────────────────────────────────────
"""
from __future__ import annotations

import difflib
import json
import re
import sys
from pathlib import Path

# Windows console (cp1252) không in được ∀∃→ hay tiếng Việt → ép UTF-8.
try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:   # noqa: BLE001 — môi trường không hỗ trợ thì bỏ qua
    pass

# ── Cho phép import package `evaluation` từ .../src ─────────────────────────────
SRC = Path(__file__).resolve().parents[2]          # FOL_Z3 → models → src
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from evaluation.fol_z3_translator import fol_string_to_z3   # noqa: E402  (raises để xem lỗi parse)

Z3_TIMEOUT_MS = 3000   # mỗi check tối đa 3s — hạ xuống nếu bài có ∀/∃ nặng

# ── Lazy-load model FOL — CHỈ nạp khi case thiếu *_fol và cần dịch NL→FOL ──────
# (giữ trong hàm để chế độ pure-FOL không kéo theo torch/model)
_FOL_MODEL = None


def _get_fol_model():
    """Nạp FOLInference 1 lần rồi tái dùng. Tốn GPU → chỉ gọi khi thật sự cần."""
    global _FOL_MODEL
    if _FOL_MODEL is None:
        from models.FOL_Z3.config import FOLz3Config
        from models.FOL_Z3.fol_inference import FOLInference
        cfg_path = SRC.parent / "configs" / "fol_z3.yaml"     # SRC=src → ../configs
        cfg = FOLz3Config.from_yaml(cfg_path) if cfg_path.is_file() else FOLz3Config()
        src = "fol_z3.yaml" if cfg_path.is_file() else "default"
        print(f"[FOL] Loading model: {cfg.fol_hub_repo_id} (config: {src}) ...")
        _FOL_MODEL = FOLInference(cfg)
    return _FOL_MODEL


# ══════════════════════════════════════════════════════════════════════════════
# Lõi solve (có trích unsat core)
# ══════════════════════════════════════════════════════════════════════════════

def _parse_premises(premises_fol: list[str], cache: dict) -> tuple[list, list]:
    """Parse từng premise → [(orig_idx, z3_expr)] OK và [(orig_idx, fol, err)] FAIL.

    Giữ NGUYÊN index gốc để unsat core map về đúng vị trí (tránh off-by-one).
    """
    ok, fail = [], []
    for idx, fol in enumerate(premises_fol):
        try:
            ok.append((idx, fol_string_to_z3(fol, cache)))
        except Exception as e:   # noqa: BLE001 — muốn THẤY lỗi parse
            fail.append((idx, fol, f"{type(e).__name__}: {e}"))
    return ok, fail


def _solver_with_tracked_premises(premises_ok: list, timeout_ms: int):
    """Solver đã add tất cả premises bằng assert_and_track (để lấy unsat core)."""
    import z3
    s = z3.Solver()
    s.set("timeout", timeout_ms)
    s.set(unsat_core=True)
    for idx, expr in premises_ok:
        s.assert_and_track(expr, z3.Bool(f"p{idx}"))   # nhãn = index gốc
    return s


def _core_indices(solver) -> list[int]:
    """unsat_core() → list index premise gốc (đã bỏ tiền tố 'p')."""
    out = []
    for c in solver.unsat_core():
        name = c.decl().name()
        if name.startswith("p") and name[1:].isdigit():
            out.append(int(name[1:]))
    return sorted(out)


def check_consistency(premises_ok: list, timeout_ms: int) -> str:
    """premises có mâu thuẫn nhau không → 'sat' | 'unsat' | 'unknown'."""
    import z3
    s = z3.Solver()
    s.set("timeout", timeout_ms)
    for _, expr in premises_ok:
        s.add(expr)
    r = s.check()
    if r == z3.sat:
        return "sat"
    if r == z3.unsat:
        return "unsat"
    return "unknown"


def entail(premises_ok: list, goal_expr, timeout_ms: int) -> tuple[str, list[int]]:
    """premises ⊨ goal? → (verdict, premises_used).

    - premises ∧ ¬goal  unsat ⟹ 'entailed'    (goal đúng)  + core
    - premises ∧  goal  unsat ⟹ 'contradicted'(goal sai)   + core
    - cả hai sat               ⟹ 'unknown'                  + []
    ¬goal/goal được add KHÔNG track → không lọt vào core ⟹ core = chỉ premises.
    """
    import z3

    s1 = _solver_with_tracked_premises(premises_ok, timeout_ms)
    s1.add(z3.Not(goal_expr))
    if s1.check() == z3.unsat:
        return "entailed", _core_indices(s1)

    s2 = _solver_with_tracked_premises(premises_ok, timeout_ms)
    s2.add(goal_expr)
    if s2.check() == z3.unsat:
        return "contradicted", _core_indices(s2)

    return "unknown", []


# ══════════════════════════════════════════════════════════════════════════════
# Normalize predicate names (Mức 1 surface + Mức 2 fuzzy có guard)
# Anchor 1 chiều: chỉ đổi tên predicate của GOAL (question/option) về vocabulary
# của PREMISES — KHÔNG đụng premises. Log mọi lần gộp để audit.
# ══════════════════════════════════════════════════════════════════════════════

FUZZY_ALIAS     = True    # Mức 2: bật alias fuzzy (có rào chắn). False = chỉ Mức 1.
FUZZY_THRESHOLD = 0.90    # ngưỡng giống tối thiểu để gộp (cùng arity)

from evaluation.fol_parser import (                       # noqa: E402
    parse_fol as _parse_fol_ast,
    PredicateNode as _Pred, NotNode as _Not,
    BinaryNode as _Bin, QuantNode as _Quant,
)


def _skey(name: str) -> str:
    """Khoá bề mặt (Mức 1): lowercase + bỏ ký tự không phải chữ/số.
    → 'PlayBasedLearning' == 'play_based_learning' == 'play__based_learning'."""
    return re.sub(r"[^a-z0-9]", "", name.lower())


def _collect_preds(ast, out: set) -> None:
    """Gom (name, arity) các predicate trong AST (bỏ số literal)."""
    if isinstance(ast, _Pred):
        if not ast.name.replace(".", "").isdigit():
            out.add((ast.name, len(ast.args)))
    elif isinstance(ast, _Not):
        _collect_preds(ast.child, out)
    elif isinstance(ast, _Bin):
        _collect_preds(ast.left, out)
        _collect_preds(ast.right, out)
    elif isinstance(ast, _Quant):
        _collect_preds(ast.body, out)


def _vocab(fol_list: list[str]) -> set:
    v: set = set()
    for f in fol_list:
        try:
            _collect_preds(_parse_fol_ast(f), v)
        except Exception:   # noqa: BLE001 — premise parse fail thì bỏ qua khỏi vocab
            pass
    return v


def canonicalize_predicates(
    goal_fol: str,
    premises_fol: list[str],
    fuzzy: bool | None = None,
    threshold: float | None = None,
) -> tuple[str, list[tuple]]:
    """Đổi tên predicate của GOAL về vocabulary PREMISES (anchor 1 chiều).

    Trả về (goal_mới, log) với log = [(old, new, 'surface'|'fuzzy', ratio)].
    Guard: chỉ gộp CÙNG ARITY; fuzzy cần ratio ≥ threshold; KHÔNG đụng premises.
    """
    fuzzy = FUZZY_ALIAS if fuzzy is None else fuzzy
    threshold = FUZZY_THRESHOLD if threshold is None else threshold

    goal_preds: set = set()
    try:
        _collect_preds(_parse_fol_ast(goal_fol), goal_preds)
    except Exception:   # noqa: BLE001 — goal parse fail → để nguyên
        return goal_fol, []

    prem = _vocab(premises_fol)
    prem_names = {n for n, _ in prem}
    prem_by_arity: dict = {}
    prem_surface: dict = {}
    for n, a in prem:
        prem_by_arity.setdefault(a, []).append(n)
        prem_surface.setdefault((_skey(n), a), n)   # đại diện đầu tiên

    renames: dict = {}
    log: list = []
    for g, a in goal_preds:
        if g in prem_names:
            continue                                       # khớp tuyệt đối → giữ
        key = (_skey(g), a)
        if key in prem_surface and prem_surface[key] != g:  # Mức 1 (surface)
            renames[g] = prem_surface[key]
            log.append((g, prem_surface[key], "surface", 1.0))
            continue
        if fuzzy:                                           # Mức 2 (fuzzy, cùng arity)
            best, best_r = None, 0.0
            for c in prem_by_arity.get(a, []):
                r = difflib.SequenceMatcher(None, _skey(g), _skey(c)).ratio()
                if r > best_r:
                    best, best_r = c, r
            if best and best_r >= threshold:
                renames[g] = best
                log.append((g, best, "fuzzy", round(best_r, 3)))

    new = goal_fol
    for old, canon in renames.items():
        new = re.sub(r"\b" + re.escape(old) + r"\b", canon, new)
    return new, log


def _print_merges(log: list) -> None:
    for old, new, kind, r in log:
        print(f"  [normalize/{kind}] {old} → {new}  ({r})")


# ══════════════════════════════════════════════════════════════════════════════
# In kết quả
# ══════════════════════════════════════════════════════════════════════════════

def _show_premise_parse(premises_fol, premises_ok, premises_fail):
    print("─" * 78)
    print(f"PREMISES: {len(premises_ok)}/{len(premises_fol)} parse OK")
    ok_by_idx = {idx: expr for idx, expr in premises_ok}
    fail_by_idx = {idx: (fol, err) for idx, fol, err in premises_fail}
    for idx, fol in enumerate(premises_fol):
        if idx in ok_by_idx:
            print(f"  [{idx}] OK   {fol}")
            print(f"        → z3: {ok_by_idx[idx]}")
        else:
            _, err = fail_by_idx[idx]
            print(f"  [{idx}] FAIL {fol}")
            print(f"        ✗ {err}")


def _show_used(label, fol_list, indices):
    if not indices:
        print(f"  {label}: (không có — core rỗng)")
        return
    print(f"  {label}: {indices}  (0-based)")
    for i in indices:
        if 0 <= i < len(fol_list):
            print(f"      [{i}] {fol_list[i]}")


def solve_case(case: dict) -> None:
    print("\n" + "=" * 78)
    print(f"CASE [{case.get('type','?')}]  {case.get('question','')}")
    print("=" * 78)

    premises_fol = case.get("premises_fol") or case.get("premises-FOL") or []
    cache: dict = {}                       # 1 cache chung cho cả bài (đồng bộ sort/predicate)

    premises_ok, premises_fail = _parse_premises(premises_fol, cache)
    _show_premise_parse(premises_fol, premises_ok, premises_fail)

    if not premises_ok:
        print("\n⚠ Không premise nào parse được → Z3 bó tay.")
        return

    print("─" * 78)
    print(f"CONSISTENCY: {check_consistency(premises_ok, Z3_TIMEOUT_MS)}")

    ctype = case.get("type", "yesno")

    if ctype == "mcq":
        print("─" * 78)
        options_fol = case.get("options_fol") or {}
        if not options_fol:                       # không có FOL sẵn → model dịch từ NL
            options_nl = case.get("options")
            if options_nl:
                options_fol = _get_fol_model().generate_options_fol(options_nl, premises_fol)
                print(f"[FOL convert] options (NL) → FOL: {options_fol}")
        if not options_fol:
            print("⚠ Thiếu cả 'options_fol' lẫn 'options' → không có gì để check.")
            return
        print("ENTAILMENT theo từng option:")
        entailed = []
        for label in sorted(options_fol):
            fol = options_fol[label]
            fol, _mg = canonicalize_predicates(fol, premises_fol)
            try:
                goal = fol_string_to_z3(fol, cache)
            except Exception as e:   # noqa: BLE001
                print(f"  {label}) PARSE FAIL: {fol}  ✗ {type(e).__name__}: {e}")
                continue
            verdict, used = entail(premises_ok, goal, Z3_TIMEOUT_MS)
            print(f"\n  {label}) {fol}")
            if _mg:
                _print_merges(_mg)
            print(f"     verdict: {verdict}")
            _show_used("premises_used", premises_fol, used)
            if verdict == "entailed":
                entailed.append((label, used))
        print("\n" + "─" * 78)
        if len(entailed) == 1:
            lbl, used = entailed[0]
            print(f"ĐÁP ÁN: {lbl}   | premises_used = {used}")
        elif len(entailed) == 0:
            print("ĐÁP ÁN: (không option nào entailed — Z3 không kết luận được)")
        else:
            labels = [l for l, _ in entailed]
            print(f"ĐÁP ÁN: nhập nhằng — {labels} cùng entailed (FOL có thể quá lỏng)")

    else:  # yesno
        print("─" * 78)
        question_fol = case.get("question_fol", "").strip()
        if not question_fol:                      # không có FOL sẵn → model dịch từ NL
            q_nl = case.get("question", "")
            if q_nl:
                question_fol = _get_fol_model().generate_question_fol(q_nl, premises_fol)
                print(f"[FOL convert] question (NL) → FOL: {question_fol!r}")
        if not question_fol.strip():
            print("⚠ Không có 'question_fol' và model cũng không dịch được question.")
            return
        question_fol, _mg = canonicalize_predicates(question_fol, premises_fol)
        if _mg:
            print("NORMALIZE (question → vocab premises):")
            _print_merges(_mg)
        try:
            goal = fol_string_to_z3(question_fol, cache)
        except Exception as e:   # noqa: BLE001
            print(f"question_fol PARSE FAIL: {question_fol}\n  ✗ {type(e).__name__}: {e}")
            return
        verdict, used = entail(premises_ok, goal, Z3_TIMEOUT_MS)
        print(f"QUESTION_FOL: {question_fol}")
        print(f"  → z3: {goal}")
        answer = {"entailed": "Yes", "contradicted": "No", "unknown": "Unknown"}[verdict]
        print(f"\nVERDICT: {verdict}  →  ĐÁP ÁN: {answer}")
        _show_used("premises_used", premises_fol, used)
        if used:
            print("\n  (lưu ý: core là MỘT tập đủ để chứng minh, không chắc trùng"
                  " nhãn idx của dataset nếu bài có nhiều đường suy luận.)")


# ══════════════════════════════════════════════════════════════════════════════
# Ví dụ có sẵn — chạy ngay `python z3_playground.py`
# ══════════════════════════════════════════════════════════════════════════════

EXAMPLES = [
    # 1) Yes/No syllogism — đúng → Yes, core = [0, 1]
    {
        "type": "yesno",
        "question": "John là Person không? (syllogism)",
        "premises_fol": ["∀x (Student(x) → Person(x))", "Student(john)"],
        "question_fol": "Person(john)",
    },
    # 1b) PARSE STRESS-TEST: FOL hình học khó (multi-char var, hàm lồng, đa lượng tử)
    #     + 1 fact để demo entailment. Kỳ vọng: Yes, core = [0, 8].
    {
        "type": "yesno",
        "question": "(stress-test) Tam giác t1 có tổng góc = 180?",
        "premises_fol": [
            "∀ABC (triangle(ABC) → (total_angle(ABC) = 180))",                                  # 0
            "∀C (∀P (chord(C) ∧ perpendicular_bisector(P, C) → passes_through_center(P)))",      # 1
            "∀ABC (∀DEF (similar(ABC, DEF) → proportional(sides(ABC), sides(DEF))))",            # 2
            "∀G (∀ABC (centroid(G, ABC) → ratio(median(G), 2, 1)))",                             # 3
            "∀T (∀O (tangent(T, O) → perpendicular(T, radius(O))))",                             # 4
            "∀C1 (∀C2 (orthogonal(C1, C2) → (distance_product(intersections, centers) = radii_product(C1, C2))))",  # 5
            "∀P (∀A (∀B (equidistant(P, A, B) → lies_on_perpendicular_bisector(P, AB))))",       # 6
            "∀ABC (right_triangle(ABC) → (median_to_hypotenuse(ABC) = halved_hypotenuse(ABC)))",  # 7
            "triangle(t1)",                                                                      # 8 (fact)
        ],
        "question_fol": "total_angle(t1) = 180",
    },
    # 2) Yes/No từ data PEP8 thật — đáp án Yes; gold idx (1-based) = [7,10]
    {
        "type": "yesno",
        "question": "Có suy ra mọi project đều optimized không? (data PEP8)",
        "premises_fol": [
            "∀x (WT(x) → O(x))",          # 0
            "∀x (¬PEP8(x) → ¬WT(x))",     # 1
            "∀x (EM(x))",                 # 2
            "∀x (WT(x))",                 # 3
            "∀x (PEP8(x) → EM(x))",       # 4
            "∀x (WT(x) → PEP8(x))",       # 5
            "∀x (WS(x) → O(x))",          # 6  ← gold 7
            "∀x (EM(x) → WT(x))",         # 7
            "∀x (O(x) → CR(x))",          # 8
            "∀x (WS(x))",                 # 9  ← gold 10
            "∀x (CR(x))",                 # 10
            "∃x (BP(x))",                 # 11
            "∃x (O(x))",                  # 12
            "∀x (¬WS(x) → ¬PEP8(x))",     # 13
        ],
        "question_fol": "∀x (O(x))",
    },
    # 3) MCQ minh hoạ — chọn option entailed
    {
        "type": "mcq",
        "question": "Kết luận nào đúng về john?",
        "premises_fol": [
            "∀x (A(x) → B(x))",   # 0
            "∀x (B(x) → C(x))",   # 1
            "A(john)",            # 2
        ],
        "options_fol": {
            "A": "C(john)",       # đúng: A→B→C
            "B": "¬B(john)",      # sai
            "C": "D(john)",       # không xác định
        },
    },
]


# Ví dụ NL → model FOL tự dịch (chạy: python z3_playground.py nl) — CẦN GPU/model.
EXAMPLES_NL = [
    # Yes/No: chỉ có 'question' (NL), không có question_fol → model dịch.
    {
        "type": "yesno",
        "question": "Is every Python project optimized?",
        "premises_fol": [
            "∀x (WellTested(x) → Optimized(x))",
            "∀x (WellTested(x))",
        ],
    },
    # MCQ: 'options' là TEXT NL → model dịch sang FOL rồi Z3 chọn đáp án.
    {
        "type": "mcq",
        "question": "Which conclusion follows from the premises?",
        "premises_fol": [
            "∀x (WellTested(x) → Optimized(x))",
            "∀x (WellTested(x) → PEP8(x))",
            "∀x (WellTested(x))",
        ],
        "options": {
            "A": "If a project is not optimized, then it is not well-tested",
            "B": "All projects are well-structured",
            "C": "Every project follows PEP 8",
            "D": "Some project is not optimized",
        },
    },
]


def main() -> None:
    try:
        import z3  # noqa: F401
    except ImportError:
        print("✗ Chưa cài z3-solver. Chạy: pip install z3-solver")
        sys.exit(1)

    if len(sys.argv) > 1:
        arg = sys.argv[1]
        if arg == "nl":
            print("(Chế độ NL → sẽ nạp model FOL để dịch question/options sang FOL)")
            cases = EXAMPLES_NL
        else:
            data = json.loads(Path(arg).read_text(encoding="utf-8"))
            cases = data if isinstance(data, list) else [data]
    else:
        print("(Ví dụ pure-FOL — không cần model. "
              "'nl' = test model dịch NL→FOL | file.json = bài của bạn)")
        cases = EXAMPLES

    for case in cases:
        solve_case(case)
    print()


if __name__ == "__main__":
    main()
