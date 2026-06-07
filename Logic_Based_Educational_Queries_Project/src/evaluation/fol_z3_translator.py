"""Chuyển đổi FOL AST (từ fol_parser) → Z3 expression.

Yêu cầu: ``pip install z3-solver``
"""
from __future__ import annotations

import re
from typing import Any

from .fol_parser import (
    ASTNode,
    BinaryNode,
    FOLParseError,
    NotNode,
    PredicateNode,
    QuantNode,
    parse_fol,
)

_z3_available: bool | None = None


def _check_z3() -> bool:
    global _z3_available
    if _z3_available is None:
        try:
            import z3  # noqa: F401
            _z3_available = True
        except ImportError:
            _z3_available = False
    return _z3_available


class FOLToZ3Error(ValueError):
    """Lỗi khi chuyển AST → Z3."""
    pass


# Sort chung cho domain hữu hạn / vô hạn
_ENTITY_SORT_NAME = "Entity"


def _get_entity_sort(cache: dict[str, Any]) -> Any:
    if _ENTITY_SORT_NAME not in cache:
        import z3
        cache[_ENTITY_SORT_NAME] = z3.DeclareSort(_ENTITY_SORT_NAME)
    return cache[_ENTITY_SORT_NAME]


# ── Type inference: hàm nào trả SỐ (Real) vs Bool ───────────────
_NUM_LITERAL = re.compile(r"^\d+(?:\.\d+)?$")
_COMP_ORDER = ("≥", "≤", ">", "<")   # so sánh thứ tự → toán hạng luôn là số
_COMP_EQ = ("=", "≠", "!=")           # đẳng thức → số hoặc entity


def _is_num_literal(name: str) -> bool:
    return bool(_NUM_LITERAL.match(name))


def _num_key(node: ASTNode):
    """(name, arity) của head-function nếu node là PredicateNode (không phải số literal), else None."""
    if isinstance(node, PredicateNode) and not _is_num_literal(node.name):
        return (node.name, len(node.args))
    return None


def _operand_numeric(node: ASTNode, numeric: set) -> bool:
    """Toán hạng là số? — literal số, hoặc head-function đã biết trả số."""
    if isinstance(node, PredicateNode):
        if _is_num_literal(node.name):
            return True
        return (node.name, len(node.args)) in numeric
    return False


def infer_numeric_funcs(ast: ASTNode) -> set:
    """Quét AST → tập ``(name, arity)`` các hàm trả SỐ (xuất hiện ở vị trí so sánh số).

    ``> < ≥ ≤`` ⇒ cả 2 toán hạng là số; ``= ≠`` là số nếu một vế là số.
    Lặp tới fixpoint để lan kiểu qua ``=`` (vd ``refund(s)=total(s)`` khi ``refund`` đã biết là số).
    """
    numeric: set = set()

    def _mark(node):
        k = _num_key(node)
        if k is not None:
            numeric.add(k)

    def _walk(node):
        if isinstance(node, NotNode):
            _walk(node.child)
        elif isinstance(node, QuantNode):
            _walk(node.body)
        elif isinstance(node, BinaryNode):
            if node.op in _COMP_ORDER:
                _mark(node.left)
                _mark(node.right)
            elif node.op in _COMP_EQ:
                if _operand_numeric(node.left, numeric) or _operand_numeric(node.right, numeric):
                    _mark(node.left)
                    _mark(node.right)
            _walk(node.left)
            _walk(node.right)

    prev = -1
    while len(numeric) != prev:   # fixpoint cho '=' chaining
        prev = len(numeric)
        _walk(ast)
    return numeric


def _entity_const(name: str, cache: dict[str, Any], var_map: dict[str, Any]) -> Any:
    """Tên → Z3 Const trên Entity sort (biến đã bound dùng var_map, còn lại là hằng)."""
    import z3
    if name in var_map:
        return var_map[name]
    key = f"const_{name}"
    if key not in cache:
        cache[key] = z3.Const(name, _get_entity_sort(cache))
    return cache[key]


def _num_term(node: ASTNode, cache: dict[str, Any], var_map: dict[str, Any]) -> Any:
    """Dựng term SỐ THỰC (Real) từ toán hạng của so sánh số."""
    import z3
    if not isinstance(node, PredicateNode):
        raise FOLToZ3Error(f"Toán hạng số không hợp lệ: {node!r}")
    name, args = node.name, node.args
    if _is_num_literal(name):
        return z3.RealVal(name)
    if len(args) == 0:                          # hằng/biến số 0-ngôi, vd M = 33
        key = f"realconst_{name}"
        if key not in cache:
            cache[key] = z3.Const(name, z3.RealSort())
        return cache[key]
    key = f"func_{name}_{len(args)}"            # hàm trả số, vd grade(s, m1)
    if key not in cache:
        entity = _get_entity_sort(cache)
        cache[key] = z3.Function(name, *([entity] * len(args)), z3.RealSort())
    return cache[key](*[_entity_const(a, cache, var_map) for a in args])


def _entity_term(node: ASTNode, cache: dict[str, Any], var_map: dict[str, Any]) -> Any:
    """Dựng term Entity từ toán hạng của đẳng thức entity (vd ``m1 = m2``)."""
    if isinstance(node, PredicateNode) and len(node.args) == 0:
        return _entity_const(node.name, cache, var_map)
    return _entity_const(repr(node), cache, var_map)


def ast_to_z3(
    node: ASTNode,
    cache: dict[str, Any],
    var_map: dict[str, Any] | None = None,
    sortmap: set | None = None,
) -> Any:
    """Chuyển ASTNode → Z3 expression.

    Parameters
    ----------
    node : ASTNode
        AST node từ ``fol_parser.parse_fol()``.
    cache : dict
        Cache chia sẻ cho ``Entity`` sort + ``Function`` declarations.
        Truyền cùng 1 dict cho tất cả premises trong 1 record.
    var_map : dict | None
        Mapping variable-name → Z3 Const (quản lý bởi quantifier).
    """
    if not _check_z3():
        raise ImportError("Cần cài z3-solver: pip install z3-solver")
    import z3

    if var_map is None:
        var_map = {}
    if sortmap is None:
        sortmap = set()
    entity = _get_entity_sort(cache)

    if isinstance(node, PredicateNode):
        name = node.name
        arity = len(node.args)
        cache_key = f"func_{name}_{arity}"
        if cache_key not in cache:
            if arity == 0:
                # 0-ary predicate → Bool constant
                cache[cache_key] = z3.Bool(name)
            else:
                arg_sorts = [entity] * arity
                cache[cache_key] = z3.Function(name, *arg_sorts, z3.BoolSort())
        func_or_const = cache[cache_key]

        if arity == 0:
            return func_or_const

        z3_args = []
        for a in node.args:
            if a in var_map:
                z3_args.append(var_map[a])
            else:
                # Constant (vd. John) hoặc variable chưa bound
                const_key = f"const_{a}"
                if const_key not in cache:
                    cache[const_key] = z3.Const(a, entity)
                z3_args.append(cache[const_key])
        return func_or_const(*z3_args)

    elif isinstance(node, NotNode):
        return z3.Not(ast_to_z3(node.child, cache, var_map, sortmap))

    elif isinstance(node, BinaryNode):
        # So sánh (≥ ≤ > < = ≠): dùng sort Real cho số học THẬT (thay vì Bool giả).
        if node.op in ("≥", "≤", ">", "<", "=", "≠", "!="):
            is_num = (
                node.op in ("≥", "≤", ">", "<")
                or _operand_numeric(node.left, sortmap)
                or _operand_numeric(node.right, sortmap)
            )
            if is_num:
                lt = _num_term(node.left, cache, var_map)
                rt = _num_term(node.right, cache, var_map)
                if node.op == ">":
                    return lt > rt
                if node.op == "<":
                    return lt < rt
                if node.op == "≥":
                    return lt >= rt
                if node.op == "≤":
                    return lt <= rt
                if node.op == "=":
                    return lt == rt
                return z3.Not(lt == rt)  # ≠, !=
            # Đẳng thức giữa entity: m1 = m2
            le = _entity_term(node.left, cache, var_map)
            re_ = _entity_term(node.right, cache, var_map)
            return (le == re_) if node.op == "=" else z3.Not(le == re_)

        left = ast_to_z3(node.left, cache, var_map, sortmap)
        right = ast_to_z3(node.right, cache, var_map, sortmap)
        if node.op == "∧":
            return z3.And(left, right)
        elif node.op == "∨":
            return z3.Or(left, right)
        elif node.op == "→":
            return z3.Implies(left, right)
        elif node.op == "↔":
            return left == right
        else:
            raise FOLToZ3Error(f"Unknown binary op: {node.op!r}")

    elif isinstance(node, QuantNode):
        v = z3.Const(node.var, entity)
        new_map = {**var_map, node.var: v}
        body = ast_to_z3(node.body, cache, new_map, sortmap)
        if node.quant == "∀":
            return z3.ForAll(v, body)
        elif node.quant == "∃":
            return z3.Exists(v, body)
        else:
            raise FOLToZ3Error(f"Unknown quantifier: {node.quant!r}")

    else:
        raise FOLToZ3Error(f"Unknown AST node type: {type(node).__name__}")


# ── Public convenience ───────────────────────────────────────


def fol_string_to_z3(fol_str: str, cache: dict[str, Any]) -> Any:
    """Parse FOL string → Z3 expression (one-shot).

    Parameters
    ----------
    fol_str : str
        FOL formula, vd. ``'∀x (Student(x) → Graduated(x))'``
    cache : dict
        Chia sẻ giữa các premises cùng record.

    Returns
    -------
    z3.ExprRef
    """
    ast = parse_fol(fol_str)
    sortmap = infer_numeric_funcs(ast)
    return ast_to_z3(ast, cache, sortmap=sortmap)


def safe_fol_string_to_z3(fol_str: str, cache: dict[str, Any]) -> Any | None:
    """Như ``fol_string_to_z3`` nhưng trả ``None`` thay vì raise."""
    try:
        return fol_string_to_z3(fol_str, cache)
    except Exception:
        return None
