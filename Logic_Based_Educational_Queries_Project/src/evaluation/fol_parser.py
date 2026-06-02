"""Tokenizer + recursive-descent parser cho FOL strings → AST nodes.

Grammar hỗ trợ (phù hợp dataset Logic_Based_Educational_Queries):

    formula     := quantified | implication
    quantified  := QUANT VAR formula            (VAR = single lowercase OR multi-char)
    implication := disjunction (('→' | '↔') disjunction)?
    disjunction := conjunction ('∨' conjunction)*
    conjunction := unary ('∧' unary)*
    unary       := '¬' unary | quantified | atom
    atom        := PREDICATE '(' arglist ')' comparison_tail?
                 | '(' formula ')'
                 | 0-ary PREDICATE comparison_tail?
                 | NUMBER comparison_tail?
    comparison_tail := COMP_OP atom    (produces BinaryNode with comparison)
    arglist     := arg (',' arg)*
    arg         := term | nested_call | quoted_string
    term        := VAR | CONSTANT | NUMBER | COMP+NUMBER
    nested_call := PREDICATE '(' arglist ')'
    quoted_string := ' ... '

Ký hiệu:
    QUANT     = ∀ | ∃
    VAR       = [a-z]  (một ký tự thường) — hoặc multi-char nếu sau quantifier
    CONSTANT  = [A-Z][a-zA-Z0-9_]* khi không phải predicate | [a-z][a-z0-9_]+ | NUMBER
    COMP_OP   = ≥ | ≤ | > | < | = | ≠ | !=
    PREDICATE = identifier theo sau bởi '('
"""
from __future__ import annotations

import re
from dataclasses import dataclass
from typing import Sequence


# ── AST nodes ────────────────────────────────────────────────

@dataclass(frozen=True)
class PredicateNode:
    """Vị từ: Student(x), Pass(x, John), depleted_fund (0-ary), 4 (number literal)."""
    name: str
    args: tuple[str, ...]
    def __repr__(self) -> str:
        if self.args:
            return f"{self.name}({', '.join(self.args)})"
        return self.name


@dataclass(frozen=True)
class NotNode:
    """Phủ định ¬."""
    child: "ASTNode"
    def __repr__(self) -> str:
        return f"¬({self.child})"


@dataclass(frozen=True)
class BinaryNode:
    """Phép nối: ∧ ∨ → ↔ = ≥ ≤ > < ≠"""
    op: str
    left: "ASTNode"
    right: "ASTNode"
    def __repr__(self) -> str:
        return f"({self.left} {self.op} {self.right})"


@dataclass(frozen=True)
class QuantNode:
    """Bộ lượng tử ∀ hoặc ∃."""
    quant: str
    var: str
    body: "ASTNode"
    def __repr__(self) -> str:
        return f"{self.quant}{self.var}({self.body})"


ASTNode = PredicateNode | NotNode | BinaryNode | QuantNode


class FOLParseError(ValueError):
    """Không parse được FOL string."""
    pass


# ── Comparison operators ────────────────────────────────────
_COMP_OPS = frozenset({"≥", "≤", ">", "<", "=", "≠", "!="})


# ── Tokenizer ────────────────────────────────────────────────

# Token regex: logic symbols → comparison → parens/comma → quoted strings → numbers → identifiers
_TOKEN_RE = re.compile(
    r"("
    r"∀|∃|→|↔|∧|∨|¬"                    # logic symbols
    r"|≥|≤|!=|≠|>=|<=|[=><]"            # comparison operators
    r"|[(),]"                            # parens, comma
    r"|'[^']*'"                          # quoted strings: '20/3/2025', '8:00'
    r"|[0-9]+(?:\.[0-9]+)?"             # numbers: 4, 0.5, 2.0, 180
    r"|[A-Za-z_][A-Za-z0-9_]*"          # identifiers
    r")"
)

# Normalize ASCII → Unicode (2 groups: symbols match anywhere, keywords need \b)
_NORMALIZE_SYMBOLS: dict[str, str] = {
    "<->": "↔", "<=>": "↔",
    "->": "→", "=>": "→",
    ">=": "≥", "<=": "≤", "!=": "≠",
    "/\\": "∧", "\\/": "∨",
    "~": "¬",
}
_NORMALIZE_KEYWORDS: dict[str, str] = {
    "forall": "∀", "exists": "∃",
    "implies": "→", "not": "¬",
    "and": "∧", "or": "∨", "iff": "↔",
}
_NORMALIZE_RE = re.compile(
    "|".join(
        [re.escape(k) for k in sorted(_NORMALIZE_SYMBOLS, key=len, reverse=True)]
        + [r"\b" + re.escape(k) + r"\b" for k in sorted(_NORMALIZE_KEYWORDS, key=len, reverse=True)]
    )
)
_NORMALIZE_MAP: dict[str, str] = {**_NORMALIZE_SYMBOLS, **_NORMALIZE_KEYWORDS}


def normalize_fol_string(s: str) -> str:
    """Chuẩn hoá ASCII → Unicode. 'Score' không bị ảnh hưởng bởi 'or' nhờ \\b."""
    return _NORMALIZE_RE.sub(lambda m: _NORMALIZE_MAP[m.group()], s)


def _sanitize_before_parse(s: str) -> str:
    """Tiền xử lý: strip trailing junk, fix unbalanced parens."""
    # Strip trailing commas, backslashes, brackets
    s = s.rstrip(", \\\t\n[]}{")
    # Fix unbalanced trailing ')'
    open_c = s.count("(")
    close_c = s.count(")")
    if close_c > open_c:
        excess = close_c - open_c
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
    """Sanitize → normalize → tokenize."""
    sanitized = _sanitize_before_parse(fol_str)
    normed = normalize_fol_string(sanitized)
    tokens = _TOKEN_RE.findall(normed)
    if not tokens:
        raise FOLParseError(f"Không tìm thấy token nào trong: {fol_str!r}")
    return tokens


# ── Recursive-descent parser ─────────────────────────────────

class FOLParser:
    """Parse tokens → ASTNode.

    Thay đổi so với phiên bản cũ:
    - Hỗ trợ comparison operators (≥, ≤, >, <, =, ≠) ở vị trí body: gpa(s) < 2.0
    - Hỗ trợ multi-char variable sau quantifier: ∀ABC(...), ∀m1(...)  → treat as variable
    - Hỗ trợ nested function calls trong args: reduce_resistance(break_into_steps(t))
    - Hỗ trợ quoted strings trong args: complete_theory(Lan, '20/3/2025')
    - Hỗ trợ ¬∀, ¬∃ (negated quantifier)
    - Hỗ trợ equality: completed_courses(sarah) = 4, M = 33
    """

    def __init__(self, tokens: Sequence[str]):
        self.tokens = list(tokens)
        self.pos = 0

    def _peek(self) -> str | None:
        return self.tokens[self.pos] if self.pos < len(self.tokens) else None

    def _peek_ahead(self, offset: int = 1) -> str | None:
        idx = self.pos + offset
        return self.tokens[idx] if idx < len(self.tokens) else None

    def _consume(self, expected: str | None = None) -> str:
        if self.pos >= len(self.tokens):
            raise FOLParseError(f"Unexpected end of tokens (expected {expected!r})")
        tok = self.tokens[self.pos]
        if expected is not None and tok != expected:
            raise FOLParseError(f"Expected {expected!r} at pos {self.pos}, got {tok!r}")
        self.pos += 1
        return tok

    def _at_end(self) -> bool:
        return self.pos >= len(self.tokens)

    def _is_ident_or_num(self, tok: str | None) -> bool:
        if tok is None:
            return False
        return tok[0].isalpha() or tok[0] == "_" or tok[0].isdigit()

    def _is_quoted(self, tok: str | None) -> bool:
        return tok is not None and tok.startswith("'") and tok.endswith("'")

    # ── grammar rules ──

    def parse(self) -> ASTNode:
        node = self._parse_formula()
        if not self._at_end():
            remaining = self.tokens[self.pos:]
            raise FOLParseError(f"Extra tokens after complete formula at pos {self.pos}: {remaining}")
        return node

    def _parse_formula(self) -> ASTNode:
        if self._peek() in ("∀", "∃"):
            return self._parse_quantified()
        return self._parse_implication()

    def _parse_quantified(self) -> ASTNode:
        """Parse ∀x/∃x ... Cho phép multi-char variable: ∀ABC, ∀m1, ∀student."""
        quant = self._consume()
        var_tok = self._consume()
        # Chấp nhận multi-char variable (ABC, m1, student) — treat as variable name
        if not var_tok or not (var_tok[0].isalpha() or var_tok[0] == "_"):
            raise FOLParseError(f"Expected variable after {quant}, got {var_tok!r}")
        # Nếu token tiếp là ',' → multiple quantified vars: ∃m1, ∃m2, ...
        # → chỉ lấy var đầu, bỏ qua phần sau comma (simplified)
        while self._peek() == ",":
            self._consume(",")  # skip comma
            next_tok = self._peek()
            if next_tok in ("∀", "∃"):
                # ∃m1, ∃m2 → skip ∃ and var
                self._consume()
                self._consume()
            elif self._is_ident_or_num(next_tok):
                self._consume()  # skip var name
        body = self._parse_formula()
        return QuantNode(quant, var_tok, body)

    def _parse_implication(self) -> ASTNode:
        """Parse A → B (right-associative)."""
        left = self._parse_disjunction()
        if self._peek() in ("→", "↔"):
            op = self._consume()
            right = self._parse_formula()
            return BinaryNode(op, left, right)
        return left

    def _parse_disjunction(self) -> ASTNode:
        left = self._parse_conjunction()
        while self._peek() == "∨":
            self._consume()
            right = self._parse_conjunction()
            left = BinaryNode("∨", left, right)
        return left

    def _parse_conjunction(self) -> ASTNode:
        left = self._parse_unary()
        while self._peek() == "∧":
            self._consume()
            right = self._parse_unary()
            left = BinaryNode("∧", left, right)
        return left

    def _parse_unary(self) -> ASTNode:
        if self._peek() == "¬":
            self._consume()
            return NotNode(self._parse_unary())
        if self._peek() in ("∀", "∃"):
            return self._parse_quantified()
        return self._parse_atom()

    def _parse_atom(self) -> ASTNode:
        tok = self._peek()
        if tok is None:
            raise FOLParseError("Unexpected end — expected atom")

        # Grouped formula: '(' formula ')'
        if tok == "(":
            self._consume("(")
            node = self._parse_formula()
            self._consume(")")
            return self._maybe_comparison_tail(node)

        # Quoted string as atom (e.g., standalone '20/3/2025')
        if self._is_quoted(tok):
            val = self._consume()
            return PredicateNode(val, ())

        # Identifier or number
        if self._is_ident_or_num(tok):
            name = self._consume()
            if self._peek() == "(":
                # Predicate with args: Student(x, John)
                self._consume("(")
                args: list[str] = []
                if self._peek() != ")":
                    args.append(self._parse_arg())
                    while self._peek() == ",":
                        self._consume(",")
                        args.append(self._parse_arg())
                self._consume(")")
                node = PredicateNode(name, tuple(args))
            else:
                node = PredicateNode(name, ())
            # Check for comparison tail: gpa(s) < 2.0, M = 33, completed_courses(sarah) = 4
            return self._maybe_comparison_tail(node)

        # Comparison operator at atom position → skip gracefully
        if tok in _COMP_OPS:
            self._consume()
            return self._parse_atom()

        raise FOLParseError(f"Unexpected token at pos {self.pos}: {tok!r}")

    def _maybe_comparison_tail(self, left: ASTNode) -> ASTNode:
        """If next token is a comparison op, parse: left OP right → BinaryNode."""
        if self._peek() in _COMP_OPS:
            op = self._consume()
            right = self._parse_atom()
            return BinaryNode(op, left, right)
        return left

    def _parse_arg(self) -> str:
        """Parse a single argument inside predicate parens.

        Supports: variable, constant, number, quoted string, comparison+number,
        nested function call: break_into_steps(t), vehicle(a), Before(June1).
        """
        tok = self._peek()
        if tok is None:
            raise FOLParseError("Unexpected end — expected argument")

        # Quoted string: '20/3/2025', '8:00'
        if self._is_quoted(tok):
            return self._consume()

        # Identifier or number
        if self._is_ident_or_num(tok):
            name = self._consume()
            # Nested function call: break_into_steps(t), vehicle(a), Before(June1)
            if self._peek() == "(":
                self._consume("(")
                inner_args = [self._parse_arg()]
                while self._peek() == ",":
                    self._consume(",")
                    inner_args.append(self._parse_arg())
                self._consume(")")
                # Return as flattened string representation
                return f"{name}({','.join(inner_args)})"
            return name

        # Comparison operator as part of arg: ≥4, ≤1
        if tok in _COMP_OPS:
            op = self._consume()
            if self._is_ident_or_num(self._peek()):
                val = self._consume()
                return f"{op}{val}"
            return op

        # Negation in arg position (rare but seen): ¬special_case(x)
        if tok == "¬":
            self._consume()
            if self._is_ident_or_num(self._peek()):
                return "¬" + self._parse_arg()
            return "¬"

        raise FOLParseError(f"Unexpected token in argument at pos {self.pos}: {tok!r}")


# ── Public API ───────────────────────────────────────────────

def parse_fol(fol_str: str) -> ASTNode:
    """Parse FOL string → ASTNode. Raises FOLParseError on failure."""
    tokens = tokenize_fol(fol_str)
    return FOLParser(tokens).parse()


def safe_parse_fol(fol_str: str) -> ASTNode | None:
    """Parse FOL string → ASTNode, hoặc None nếu thất bại."""
    try:
        return parse_fol(fol_str)
    except (FOLParseError, Exception):
        return None
