"""Tokenizer + recursive-descent parser cho FOL strings → AST nodes.

Grammar hỗ trợ (phù hợp dataset Logic_Based_Educational_Queries):

    formula     := quantified | implication
    quantified  := QUANT VAR formula
    implication := disjunction (('→' | '↔') disjunction)?
    disjunction := conjunction ('∨' conjunction)*
    conjunction := unary ('∧' unary)*
    unary       := '¬' unary | atom
    atom        := PREDICATE '(' arglist ')' | '(' formula ')'
    arglist     := term (',' term)*
    term        := VAR | CONSTANT

Ký hiệu:
    QUANT     = ∀ | ∃
    VAR       = [a-z]  (một ký tự thường)
    CONSTANT  = [a-z][a-z0-9_]+  (nhiều ký tự thường — tên riêng viết thường)
               | [A-Z][a-z0-9_]+  khi không phải predicate (context-dependent)
    PREDICATE = [A-Z][a-zA-Z0-9_]*  (CamelCase hoặc 1 ký tự hoa)
"""
from __future__ import annotations

import re
from dataclasses import dataclass
from typing import Sequence


# ── AST nodes ────────────────────────────────────────────────


@dataclass(frozen=True)
class PredicateNode:
    name: str
    args: tuple[str, ...]

    def __repr__(self) -> str:
        return f"{self.name}({', '.join(self.args)})"


@dataclass(frozen=True)
class NotNode:
    child: "ASTNode"

    def __repr__(self) -> str:
        return f"¬({self.child})"


@dataclass(frozen=True)
class BinaryNode:
    op: str  # '∧' | '∨' | '→' | '↔'
    left: "ASTNode"
    right: "ASTNode"

    def __repr__(self) -> str:
        return f"({self.left} {self.op} {self.right})"


@dataclass(frozen=True)
class QuantNode:
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

# Thứ tự quan trọng: ký hiệu logic trước, rồi identifier (predicate/var/const), rồi dấu câu.
_TOKEN_RE = re.compile(
    r"(∀|∃|→|↔|∧|∨|¬|[(),]|[A-Za-z_][A-Za-z0-9_]*)"
)

# Các ký hiệu thay thế ASCII thường gặp → chuẩn hoá sang Unicode
_NORMALIZE_MAP: dict[str, str] = {
    "->": "→",
    "=>": "→",
    "<->": "↔",
    "<=>": "↔",
    "/\\": "∧",
    "\\/": "∨",
    "~": "¬",
    "!": "¬",
    "forall": "∀",
    "exists": "∃",
    "not": "¬",
    "and": "∧",
    "or": "∨",
    "implies": "→",
    "iff": "↔",
}

_NORMALIZE_RE = re.compile(
    "|".join(re.escape(k) for k in sorted(_NORMALIZE_MAP, key=len, reverse=True))
)


def normalize_fol_string(s: str) -> str:
    """Chuẩn hoá ASCII alternatives → ký hiệu Unicode chuẩn."""
    return _NORMALIZE_RE.sub(lambda m: _NORMALIZE_MAP[m.group()], s)


def tokenize_fol(fol_str: str) -> list[str]:
    """Tách FOL string thành danh sách token."""
    normed = normalize_fol_string(fol_str)
    tokens = _TOKEN_RE.findall(normed)
    if not tokens:
        raise FOLParseError(f"Không tìm thấy token nào trong: {fol_str!r}")
    return tokens


# ── Heuristic: phân biệt predicate vs constant ──────────────
# Predicate: theo sau bởi '(' — vd. Student(
# Constant: chữ hoa đầu nhưng KHÔNG theo sau bởi '(' — vd. John
# Variable: chữ thường 1 ký tự — vd. x, y, z

def _classify_tokens(tokens: list[str]) -> dict[str, str]:
    """Trả về mapping identifier → 'predicate' | 'constant' | 'variable'."""
    classes: dict[str, str] = {}
    for i, tok in enumerate(tokens):
        if not tok[0].isalpha() and tok[0] != "_":
            continue
        if tok in ("∀", "∃", "∧", "∨", "¬", "→", "↔"):
            continue
        # Chữ thường 1 ký tự → variable
        if len(tok) == 1 and tok.islower():
            classes.setdefault(tok, "variable")
            continue
        # Theo sau bởi '(' → predicate
        if i + 1 < len(tokens) and tokens[i + 1] == "(":
            classes[tok] = "predicate"
            continue
        # Chữ hoa đầu, không theo sau '(' → constant
        if tok[0].isupper() and tok not in classes:
            classes[tok] = "constant"
        elif tok[0].islower() and len(tok) > 1 and tok not in classes:
            classes[tok] = "constant"
    return classes


# ── Recursive-descent parser ─────────────────────────────────


class FOLParser:
    """Parse list[str] tokens → ASTNode."""

    def __init__(self, tokens: Sequence[str]):
        self.tokens = list(tokens)
        self.pos = 0

    # ── helpers ──

    def _peek(self) -> str | None:
        return self.tokens[self.pos] if self.pos < len(self.tokens) else None

    def _consume(self, expected: str | None = None) -> str:
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
        return self.pos >= len(self.tokens)

    # ── grammar rules ──

    def parse(self) -> ASTNode:
        node = self._parse_formula()
        if not self._at_end():
            remaining = self.tokens[self.pos:]
            raise FOLParseError(
                f"Extra tokens after complete formula at pos {self.pos}: {remaining}"
            )
        return node

    def _parse_formula(self) -> ASTNode:
        if self._peek() in ("∀", "∃"):
            return self._parse_quantified()
        return self._parse_implication()

    def _parse_quantified(self) -> ASTNode:
        quant = self._consume()
        var = self._consume()
        if len(var) != 1 or not var.islower():
            raise FOLParseError(
                f"Expected variable (single lowercase) after {quant}, got {var!r}"
            )
        body = self._parse_formula()
        return QuantNode(quant, var, body)

    def _parse_implication(self) -> ASTNode:
        left = self._parse_disjunction()
        if self._peek() in ("→", "↔"):
            op = self._consume()
            right = self._parse_formula()  # right-associative; cho phép ∀/∃ bên phải
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
            return node
        # Predicate(args...)
        if tok[0].isalpha() or tok[0] == "_":
            name = self._consume()
            if self._peek() == "(":
                self._consume("(")
                args = [self._consume()]
                while self._peek() == ",":
                    self._consume(",")
                    args.append(self._consume())
                self._consume(")")
                return PredicateNode(name, tuple(args))
            else:
                # Bare predicate without args — treat as 0-ary
                return PredicateNode(name, ())
        raise FOLParseError(f"Unexpected token at pos {self.pos}: {tok!r}")


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
