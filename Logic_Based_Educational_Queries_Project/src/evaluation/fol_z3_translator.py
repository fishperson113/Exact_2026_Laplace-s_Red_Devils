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


def ast_to_z3(
    node: ASTNode,
    cache: dict[str, Any],
    var_map: dict[str, Any] | None = None,
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
        return z3.Not(ast_to_z3(node.child, cache, var_map))

    elif isinstance(node, BinaryNode):
        # Comparison operators (≥, ≤, >, <, =, ≠): treat as boolean predicates
        # vì Z3 Entity sort không hỗ trợ arithmetic — encode thành Bool predicate
        if node.op in ("≥", "≤", ">", "<", "=", "≠", "!="):
            # Flatten left and right thành string representation → Bool predicate
            left_str = repr(node.left) if not isinstance(node.left, PredicateNode) else repr(node.left)
            right_str = repr(node.right) if not isinstance(node.right, PredicateNode) else repr(node.right)
            comp_name = f"_cmp_{left_str}_{node.op}_{right_str}"
            # Sanitize name cho Z3
            comp_name = re.sub(r"[^A-Za-z0-9_]", "_", comp_name)
            cache_key = f"comp_{comp_name}"
            if cache_key not in cache:
                cache[cache_key] = z3.Bool(comp_name)
            return cache[cache_key]

        left = ast_to_z3(node.left, cache, var_map)
        right = ast_to_z3(node.right, cache, var_map)
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
        body = ast_to_z3(node.body, cache, new_map)
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
    return ast_to_z3(ast, cache)


def safe_fol_string_to_z3(fol_str: str, cache: dict[str, Any]) -> Any | None:
    """Như ``fol_string_to_z3`` nhưng trả ``None`` thay vì raise."""
    try:
        return fol_string_to_z3(fol_str, cache)
    except Exception:
        return None
