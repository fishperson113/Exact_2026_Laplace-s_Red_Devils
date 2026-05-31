"""Tokenizer + recursive-descent parser cho FOL strings → AST nodes.

Grammar hỗ trợ (phù hợp dataset Logic_Based_Educational_Queries):

    formula     := quantified | implication
    quantified  := QUANT VAR formula
    implication := disjunction (('→' | '↔') disjunction)?
    disjunction := conjunction ('∨' conjunction)*
    conjunction := unary ('∧' unary)*
    unary       := '¬' unary | quantified | atom
    atom        := PREDICATE '(' arglist ')' | '(' formula ')' | 0-ary PREDICATE
    arglist     := term (',' term)*
    term        := VAR | CONSTANT | NUMBER

Ký hiệu:
    QUANT     = ∀ | ∃
    VAR       = [a-z]  (một ký tự thường)
    CONSTANT  = [a-z][a-z0-9_]+  (nhiều ký tự thường — tên riêng viết thường)
               | [A-Z][a-z0-9_]+  khi không phải predicate (context-dependent)
    NUMBER    = [0-9]+  (hằng số số, vd. 4, 15)
    PREDICATE = [A-Z][a-zA-Z0-9_]*  (CamelCase hoặc 1 ký tự hoa)

Ví dụ parse:
    "∀x (Student(x) → Pass(x))"
    → QuantNode("∀", "x", BinaryNode("→", PredicateNode("Student",("x",)), PredicateNode("Pass",("x",))))

    "¬∃x (Enrolled(x))"
    → NotNode(QuantNode("∃", "x", PredicateNode("Enrolled",("x",))))

    "Pass(John)"
    → PredicateNode("Pass", ("John",))
"""
from __future__ import annotations

import re
from dataclasses import dataclass
from typing import Sequence


# ── AST nodes ────────────────────────────────────────────────
# Mỗi node đại diện 1 thành phần trong cây cú pháp FOL.


@dataclass(frozen=True)
class PredicateNode:
    """Vị từ có tên và danh sách đối số.
    Ví dụ: Student(x)     → PredicateNode("Student", ("x",))
            Pass(x, John) → PredicateNode("Pass", ("x", "John"))
            depleted_fund → PredicateNode("depleted_fund", ())  # 0-ary
    """
    name: str
    args: tuple[str, ...]

    def __repr__(self) -> str:
        return f"{self.name}({', '.join(self.args)})"


@dataclass(frozen=True)
class NotNode:
    """Phủ định ¬.
    Ví dụ: ¬P(x)         → NotNode(PredicateNode("P", ("x",)))
            ¬∀x P(x)     → NotNode(QuantNode("∀", "x", ...))
    """
    child: "ASTNode"

    def __repr__(self) -> str:
        return f"¬({self.child})"


@dataclass(frozen=True)
class BinaryNode:
    """Phép nối nhị phân: ∧ (and), ∨ (or), → (implies), ↔ (iff).
    Ví dụ: P(x) → Q(x)  → BinaryNode("→", P(x), Q(x))
            A ∧ B ∧ C    → BinaryNode("∧", BinaryNode("∧", A, B), C)  # left-assoc
            A → B → C    → BinaryNode("→", A, BinaryNode("→", B, C))  # right-assoc
    """
    op: str  # '∧' | '∨' | '→' | '↔'
    left: "ASTNode"
    right: "ASTNode"

    def __repr__(self) -> str:
        return f"({self.left} {self.op} {self.right})"


@dataclass(frozen=True)
class QuantNode:
    """Bộ lượng tử ∀ (universal) hoặc ∃ (existential).
    Ví dụ: ∀x (P(x) → Q(x))  → QuantNode("∀", "x", BinaryNode("→", P, Q))
            ∃x (P(x) ∧ Q(x))  → QuantNode("∃", "x", BinaryNode("∧", P, Q))
    """
    quant: str  # '∀' | '∃'
    var: str
    body: "ASTNode"

    def __repr__(self) -> str:
        return f"{self.quant}{self.var}({self.body})"


ASTNode = PredicateNode | NotNode | BinaryNode | QuantNode


# ── FOL Parse Error ─────────────────────────────────────────


class FOLParseError(ValueError):
    """Không parse được FOL string."""
    pass


# ── Tokenizer ────────────────────────────────────────────────

# Regex tách FOL string thành tokens.
# Thứ tự ưu tiên: ký hiệu logic → so sánh → ngoặc/phẩy → số → identifier.
#
# Ví dụ: "∀x (Score(x, Calc1, 4) → Pass(x))"
# → ["∀", "x", "(", "Score", "(", "x", ",", "Calc1", ",", "4", ")", "→", "Pass", "(", "x", ")", ")"]
_TOKEN_RE = re.compile(
    r"("
    r"∀|∃|→|↔|∧|∨|¬"           # Ký hiệu logic: ∀ ∃ → ↔ ∧ ∨ ¬
    r"|≥|≤|>=|<=|!=|[=><]"      # Phép so sánh: ≥ ≤ > < =
    r"|[(),]"                    # Dấu ngoặc và phẩy
    r"|[0-9]+[A-Za-z_+]*"       # Số, có thể kèm suffix: 4, 4plus, 15
    r"|[A-Za-z_][A-Za-z0-9_]*"  # Identifier: Student, x, Calc1, depleted_fund
    r")"
)

# ── Normalize: chuẩn hóa ASCII alternatives → Unicode ───────
# Chia 2 nhóm:
#   - Symbols: match anywhere (vd. "->" không bao giờ nằm trong tên predicate)
#   - Keywords: match với \b word boundary (tránh "Score" → "Sc∨e" vì "or" trong "Score")
#
# Ví dụ:
#   "forall x (P(x) -> Q(x))"  →  "∀ x (P(x) → Q(x))"
#   "Score(x) or Q(x)"         →  "Score(x) ∨ Q(x)"     (chỉ "or" standalone bị replace)
#   "Score(x)"                  →  "Score(x)"             ("or" trong Score KHÔNG bị replace)

_NORMALIZE_SYMBOLS: dict[str, str] = {
    "<->": "↔",   # biconditional
    "<=>": "↔",
    "->": "→",    # implication
    "=>": "→",
    ">=": "≥",    # comparison
    "<=": "≤",
    "/\\": "∧",   # conjunction
    "\\/": "∨",   # disjunction
    "~": "¬",     # negation
}

_NORMALIZE_KEYWORDS: dict[str, str] = {
    "forall": "∀",    # universal quantifier
    "exists": "∃",    # existential quantifier
    "implies": "→",
    "not": "¬",
    "and": "∧",
    "or": "∨",
    "iff": "↔",
}

# Build regex: symbols match anywhere, keywords cần \b để không match substring
# Ví dụ: r"\bor\b" match "P or Q" nhưng KHÔNG match "Score"
_NORMALIZE_RE = re.compile(
    "|".join(
        [re.escape(k) for k in sorted(_NORMALIZE_SYMBOLS, key=len, reverse=True)]
        + [r"\b" + re.escape(k) + r"\b" for k in sorted(_NORMALIZE_KEYWORDS, key=len, reverse=True)]
    )
)

_NORMALIZE_MAP: dict[str, str] = {**_NORMALIZE_SYMBOLS, **_NORMALIZE_KEYWORDS}


def normalize_fol_string(s: str) -> str:
    """Chuẩn hoá ASCII alternatives → ký hiệu Unicode chuẩn.

    Ví dụ: "forall x (P(x) -> Q(x))"  →  "∀ x (P(x) → Q(x))"
    """
    return _NORMALIZE_RE.sub(lambda m: _NORMALIZE_MAP[m.group()], s)


def _sanitize_before_parse(s: str) -> str:
    """Tiền xử lý FOL string trước khi tokenize.

    Sửa ngoặc đóng thừa ở cuối (model đôi khi sinh thừa ')').

    Ví dụ: "∀x (P(x) → Q(x))))"   ← 2 dấu ) thừa
            → đếm: ( = 2, ) = 4, excess = 2
            → xóa 2 dấu ) cuối
            → "∀x (P(x) → Q(x))"
    """
    open_count = s.count("(")
    close_count = s.count(")")
    if close_count > open_count:
        excess = close_count - open_count
        # Xóa excess dấu ')' từ cuối chuỗi về đầu
        result = list(s)
        removed = 0
        for i in range(len(result) - 1, -1, -1):
            if removed >= excess:
                break
            if result[i] == ")":
                result[i] = ""
                removed += 1
        s = "".join(result)
    return s


def tokenize_fol(fol_str: str) -> list[str]:
    """Tách FOL string thành danh sách token.

    Pipeline: sanitize (sửa ngoặc) → normalize (ASCII→Unicode) → regex split

    Ví dụ: "forall x (P(x) -> Q(x))))"
            → sanitize: "forall x (P(x) -> Q(x))"     (bỏ 2 ')' thừa)
            → normalize: "∀ x (P(x) → Q(x))"          (forall→∀, ->→→)
            → tokens: ["∀", "x", "(", "P", "(", "x", ")", "→", "Q", "(", "x", ")", ")"]
    """
    sanitized = _sanitize_before_parse(fol_str)
    normed = normalize_fol_string(sanitized)
    tokens = _TOKEN_RE.findall(normed)
    if not tokens:
        raise FOLParseError(f"Không tìm thấy token nào trong: {fol_str!r}")
    return tokens


# ── Heuristic: phân biệt predicate vs constant ──────────────
# Quy tắc:
#   - Theo sau bởi '(' → predicate:  Student(   → predicate
#   - Chữ hoa đầu, không '(' → constant:  John  → constant
#   - Chữ thường 1 ký tự → variable:  x, y, z   → variable
#   - Chữ thường nhiều ký tự → constant:  john   → constant

def _classify_tokens(tokens: list[str]) -> dict[str, str]:
    """Trả về mapping identifier → 'predicate' | 'constant' | 'variable'.

    Ví dụ: tokens = ["∀", "x", "(", "Student", "(", "x", ")", "→", "Pass", "(", "John", ")", ")"]
           → {"Student": "predicate", "x": "variable", "Pass": "predicate", "John": "constant"}
    """
    classes: dict[str, str] = {}
    for i, tok in enumerate(tokens):
        if not tok[0].isalpha() and tok[0] != "_":
            continue
        if tok in ("∀", "∃", "∧", "∨", "¬", "→", "↔"):
            continue
        # "x", "y", "z" → variable (1 ký tự thường)
        if len(tok) == 1 and tok.islower():
            classes.setdefault(tok, "variable")
            continue
        # "Student(" → predicate (theo sau bởi '(')
        if i + 1 < len(tokens) and tokens[i + 1] == "(":
            classes[tok] = "predicate"
            continue
        # "John" → constant (chữ hoa đầu, không có '(' theo sau)
        if tok[0].isupper() and tok not in classes:
            classes[tok] = "constant"
        # "john" (nhiều ký tự thường) → constant
        elif tok[0].islower() and len(tok) > 1 and tok not in classes:
            classes[tok] = "constant"
    return classes


# ── Recursive-descent parser ─────────────────────────────────
#
# Thứ tự ưu tiên (precedence) từ thấp → cao:
#   formula → quantified → implication(→,↔) → disjunction(∨) → conjunction(∧) → unary(¬) → atom
#
# Ưu tiên cao hơn = bind chặt hơn.
# Ví dụ: "A ∨ B ∧ C" → "A ∨ (B ∧ C)"  vì ∧ có precedence cao hơn ∨.


class FOLParser:
    """Parse list[str] tokens → ASTNode.

    Ví dụ:
        tokens = ["∀", "x", "(", "P", "(", "x", ")", "→", "Q", "(", "x", ")", ")"]
        parser = FOLParser(tokens)
        ast = parser.parse()
        → QuantNode("∀", "x", BinaryNode("→", P(x), Q(x)))
    """

    def __init__(self, tokens: Sequence[str]):
        self.tokens = list(tokens)
        self.pos = 0  # vị trí hiện tại trong danh sách tokens

    # ── helpers ──

    def _peek(self) -> str | None:
        """Xem token hiện tại mà KHÔNG consume.
        Ví dụ: tokens=["∀","x",...], pos=0 → _peek() = "∀"
        """
        return self.tokens[self.pos] if self.pos < len(self.tokens) else None

    def _consume(self, expected: str | None = None) -> str:
        """Ăn token hiện tại và tiến pos lên 1.
        Nếu expected != None, kiểm tra token có đúng không.

        Ví dụ: tokens=["∀","x"], pos=0
                _consume() → return "∀", pos=1
                _consume("x") → return "x", pos=2
                _consume("(") → 💥 FOLParseError vì token là "x" ≠ "("
        """
        if self.pos >= len(self.tokens):
            raise FOLParseError(
                f"Unexpected end of tokens (expected {expected!r})"
            )
        tok = self.tokens[self.pos]
        if expected is not None and tok != expected:
            raise FOLParseError(
                f"Expected {expected!r} at pos {self.pos}, got {tok!r}"
            )
        self.pos += 1
        return tok

    def _at_end(self) -> bool:
        """Đã hết tokens chưa."""
        return self.pos >= len(self.tokens)

    def _is_identifier_or_number(self, tok: str | None) -> bool:
        """Token có phải identifier (predicate/var/const) hoặc số không.
        Ví dụ: "Student"→True, "x"→True, "4"→True, "→"→False, None→False
        """
        if tok is None:
            return False
        return tok[0].isalpha() or tok[0] == "_" or tok[0].isdigit()

    # ── grammar rules ──

    def parse(self) -> ASTNode:
        """Entry point. Parse toàn bộ tokens thành 1 AST node.
        Sau khi parse xong, kiểm tra không còn tokens thừa.

        Ví dụ OK:   "∀x P(x)"         → parse xong, hết tokens ✓
        Ví dụ FAIL: "∀x P(x) ) )"     → parse xong P(x) nhưng còn "))") 💥
        """
        node = self._parse_formula()
        if not self._at_end():
            remaining = self.tokens[self.pos:]
            raise FOLParseError(
                f"Extra tokens after complete formula at pos {self.pos}: {remaining}"
            )
        return node

    def _parse_formula(self) -> ASTNode:
        """Parse 1 formula. Nếu bắt đầu bằng ∀/∃ → quantified, còn lại → implication.

        Ví dụ: "∀x (P(x) → Q(x))"  → peek="∀" → đi parse_quantified
                "P(x) → Q(x)"       → peek="P" → đi parse_implication
        """
        if self._peek() in ("∀", "∃"):
            return self._parse_quantified()
        return self._parse_implication()

    def _parse_quantified(self) -> ASTNode:
        """Parse ∀x ... hoặc ∃x ...
        Quantifier + biến (1 ký tự lowercase) + body (đệ quy parse_formula).

        Ví dụ: "∀x (P(x) → Q(x))"
                → consume "∀"
                → consume "x" (check: len=1, lowercase ✓)
                → body = parse_formula("(P(x) → Q(x))")
                → QuantNode("∀", "x", ...)

        Fail:   "∀student P(student)"
                → consume "∀"
                → consume "student" → len=7, NOT single char → 💥
        """
        quant = self._consume()  # ăn "∀" hoặc "∃"
        var = self._consume()    # ăn biến
        if len(var) != 1 or not var.islower():
            raise FOLParseError(
                f"Expected variable (single lowercase) after {quant}, got {var!r}"
            )
        body = self._parse_formula()  # đệ quy parse phần thân
        return QuantNode(quant, var, body)

    def _parse_implication(self) -> ASTNode:
        """Parse A → B hoặc A ↔ B.
        Right-associative: A → B → C = A → (B → C).

        Ví dụ: "P(x) → Q(x) → R(x)"
                → left = P(x)
                → peek = "→", consume
                → right = parse_formula("Q(x) → R(x)")  ← đệ quy lên formula
                          → Q(x) → R(x)
                → BinaryNode("→", P(x), BinaryNode("→", Q(x), R(x)))

        Right-assoc vì gọi parse_formula (không phải parse_disjunction) cho vế phải,
        cho phép ∀/∃ xuất hiện bên phải: "P(x) → ∀x Q(x)"
        """
        left = self._parse_disjunction()
        if self._peek() in ("→", "↔"):
            op = self._consume()
            right = self._parse_formula()  # right-associative
            return BinaryNode(op, left, right)
        return left

    def _parse_disjunction(self) -> ASTNode:
        """Parse A ∨ B ∨ C ... (left-associative).
        ∨ có precedence THẤP hơn ∧.

        Ví dụ: "A(x) ∨ B(x) ∨ C(x)"
                → left = A(x)
                → peek="∨", consume, right = B(x) → left = (A∨B)
                → peek="∨", consume, right = C(x) → left = ((A∨B)∨C)

        Precedence: "A ∨ B ∧ C" → disjunction gọi conjunction
                → left_disj = A
                → right_disj = conjunction("B ∧ C") = (B∧C)
                → kết quả: A ∨ (B∧C)    ← ∧ bind chặt hơn ∨
        """
        left = self._parse_conjunction()
        while self._peek() == "∨":
            self._consume()
            right = self._parse_conjunction()
            left = BinaryNode("∨", left, right)
        return left

    def _parse_conjunction(self) -> ASTNode:
        """Parse A ∧ B ∧ C ... (left-associative).
        ∧ có precedence CAO hơn ∨ nhưng THẤP hơn ¬.

        Ví dụ: "P(x) ∧ Q(x) ∧ R(x)"
                → ((P(x) ∧ Q(x)) ∧ R(x))
        """
        left = self._parse_unary()
        while self._peek() == "∧":
            self._consume()
            right = self._parse_unary()
            left = BinaryNode("∧", left, right)
        return left

    def _parse_unary(self) -> ASTNode:
        """Parse ¬A (negation) hoặc quantifier ở vị trí unary.
        ¬ có precedence CAO nhất trong các connectives.

        Ví dụ 1 — negation:
            "¬P(x)"      → consume "¬" → đệ quy → NotNode(P(x))
            "¬¬P(x)"     → consume "¬" → đệ quy → NotNode(NotNode(P(x)))

        Ví dụ 2 — negated quantifier (FIX cho ¬∀, ¬∃):
            "¬∀x P(x)"   → consume "¬" → đệ quy _parse_unary
                          → peek = "∀" → _parse_quantified → QuantNode(...)
                          → NotNode(QuantNode("∀", "x", P(x)))

        Ví dụ 3 — quantifier sau ∧ (P(x) ∧ ∀x Q(x)):
            conjunction gọi _parse_unary cho vế phải
            → peek = "∀" → _parse_quantified
            → QuantNode("∀", "x", Q(x))
        """
        if self._peek() == "¬":
            self._consume()
            return NotNode(self._parse_unary())
        # Cho phép quantifier ở vị trí unary
        # → hỗ trợ: ¬∀x ..., ¬∃x ..., P(x) ∧ ∀x Q(x), P(x) ∨ ∃x Q(x)
        if self._peek() in ("∀", "∃"):
            return self._parse_quantified()
        return self._parse_atom()

    def _parse_atom(self) -> ASTNode:
        """Parse thành phần cơ bản nhất:
        - (formula)       : nhóm bằng ngoặc
        - Predicate(args) : vị từ có đối số
        - Predicate       : vị từ 0-ary (không đối số)
        - ≥, ≤, =, >, <  : skip comparison operators (graceful recovery)

        Ví dụ 1 — nhóm ngoặc:
            "(P(x) → Q(x))" → consume "(" → parse_formula → consume ")"

        Ví dụ 2 — predicate có args:
            "Student(x, John)" → consume "Student" → peek="(" → parse args
            → PredicateNode("Student", ("x", "John"))

        Ví dụ 3 — predicate 0-ary:
            "depleted_fund"  → consume "depleted_fund" → peek ≠ "("
            → PredicateNode("depleted_fund", ())

        Ví dụ 4 — comparison operator (skip):
            "≥ 2"  ← khi gặp ≥ ở vị trí atom (model sinh sai)
            → skip "≥" → parse_atom tiếp → "2" → PredicateNode("2", ())
        """
        tok = self._peek()
        if tok is None:
            raise FOLParseError("Unexpected end — expected atom")
        # Case 1: grouped formula '(' ... ')'
        if tok == "(":
            self._consume("(")
            node = self._parse_formula()
            self._consume(")")
            return node
        # Case 2: Predicate(args...) hoặc bare identifier (0-ary)
        if self._is_identifier_or_number(tok):
            name = self._consume()
            if self._peek() == "(":
                # Có args: Student(x, John)
                self._consume("(")
                args: list[str] = []
                if self._peek() != ")":
                    args.append(self._parse_term())
                    while self._peek() == ",":
                        self._consume(",")
                        args.append(self._parse_term())
                self._consume(")")
                return PredicateNode(name, tuple(args))
            else:
                # 0-ary: depleted_fund (không có ngoặc)
                return PredicateNode(name, ())
        # Case 3: comparison operators — skip gracefully
        # Khi model sinh "delay(x) ≥ 2", parser gặp ≥ ở vị trí atom
        # → skip nó và tiếp tục parse phần sau
        if tok in ("≥", "≤", "=", ">", "<"):
            self._consume()
            return self._parse_atom()
        raise FOLParseError(f"Unexpected token at pos {self.pos}: {tok!r}")

    def _parse_term(self) -> str:
        """Parse 1 term trong danh sách đối số: biến, hằng, số, hoặc comparison+số.

        Ví dụ 1 — identifier/number:
            "x"      → consume → "x"       (variable)
            "John"   → consume → "John"    (constant)
            "4"      → consume → "4"       (number)
            "Calc1"  → consume → "Calc1"   (constant)

        Ví dụ 2 — comparison gộp với số:
            "≥4"     ← 2 tokens: "≥" + "4"
            → consume "≥" + consume "4" → gộp thành "≥4"
            Dùng cho: Score(x, Calc1, ≥4)
        """
        tok = self._peek()
        if tok is None:
            raise FOLParseError("Unexpected end — expected term in argument list")
        # Variable, constant, number
        if self._is_identifier_or_number(tok):
            return self._consume()
        # Comparison + number: "≥" + "4" → "≥4"
        if tok in ("≥", "≤", "=", ">", "<"):
            op = self._consume()
            if self._is_identifier_or_number(self._peek()):
                val = self._consume()
                return f"{op}{val}"
            return op
        raise FOLParseError(f"Unexpected token in argument list at pos {self.pos}: {tok!r}")


# ── Public API ───────────────────────────────────────────────


def parse_fol(fol_str: str) -> ASTNode:
    """Parse FOL string → ASTNode. Raises FOLParseError on failure.

    Pipeline: sanitize → normalize → tokenize → recursive descent parse

    Ví dụ: parse_fol("∀x (Student(x) → Pass(x))")
           → QuantNode("∀", "x", BinaryNode("→", Student(x), Pass(x)))
    """
    tokens = tokenize_fol(fol_str)
    return FOLParser(tokens).parse()


def safe_parse_fol(fol_str: str) -> ASTNode | None:
    """Parse FOL string → ASTNode, hoặc None nếu thất bại.
    Không raise exception — dùng khi cần check parse được hay không.

    Ví dụ: safe_parse_fol("∀x P(x)")        → QuantNode(...)
            safe_parse_fol("invalid !!!")     → None
    """
    try:
        return parse_fol(fol_str)
    except (FOLParseError, Exception):
        return None
