from typing import Union, Optional

from pynescript.ast.types import AST


def _dump_value_impl(value, indent: int = 0, depth: int = 0):
    indent_step = " " * indent
    if isinstance(value, AST):
        return _dump_impl(value, indent=indent, depth=depth)
    elif isinstance(value, list) and len(value) > 0:
        lines = []
        lines.append("[")
        for subvalue in value:
            lines.append(
                f"{indent_step * (depth + 1)}{_dump_value_impl(subvalue, indent=indent, depth=depth + 1)},"
            )
        lines.append(f"{indent_step * depth}]")
        return "\n".join(lines)
    else:
        return f"{value!r}"


def _dump_impl(node: AST, indent: int = 0, depth: int = 0):
    class_name = node.__class__.__name__
    class_params_except = [
        "loc",
        "end_loc",
        "lineno",
        "col_offset",
        "end_lineno",
        "end_col_offset",
    ]
    class_params = {
        name: value
        for name, value in node.__dict__.items()
        if name not in class_params_except
    }
    if indent > 0 and len(class_params) > 0:
        indent_step = " " * indent
        lines = []
        lines.append(f"{class_name}(")
        for name, value in class_params.items():
            lines.append(
                f"{indent_step * (depth + 1)}{name}={_dump_value_impl(value, indent=indent, depth=depth + 1)},"
            )
        lines.append(f"{indent_step * depth})")
        return "\n".join(lines)
    else:
        class_params = [f"{name}={value!r}" for name, value in class_params.items()]
        class_params = ", ".join(class_params)
        return f"{class_name}({class_params})"


def dump(node: AST, indent: Optional[int] = None) -> str:
    if indent is None:
        indent = 2

    return _dump_impl(node, indent=indent)


def literal_eval(node_or_string: Union[str, AST]):
    raise NotImplementedError()
