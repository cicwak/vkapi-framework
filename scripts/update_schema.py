#!/usr/bin/env python3
from __future__ import annotations

import json
import keyword
import re
import urllib.request
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "src" / "vkapi" / "methods" / "generated.py"
BASE_URL = "https://raw.githubusercontent.com/VKCOM/vk-api-schema/master"
TREE_URL = "https://api.github.com/repos/VKCOM/vk-api-schema/git/trees/master?recursive=1"
USER_AGENT = {"User-Agent": "vkapi-codegen"}


def fetch_json(url: str) -> Any:
    req = urllib.request.Request(url, headers=USER_AGENT)
    with urllib.request.urlopen(req, timeout=60) as response:
        return json.load(response)


def snake(name: str) -> str:
    value = re.sub(r"(?<!^)(?=[A-Z])", "_", name).replace("-", "_").lower()
    if keyword.iskeyword(value):
        value += "_"
    return value


def pascal(name: str) -> str:
    parts = re.split(r"[._-]", name)
    return "".join(part[:1].upper() + part[1:] for part in parts if part)


def annotation(param: dict[str, Any]) -> str:
    value_type = param.get("type")
    if isinstance(value_type, list):
        types = sorted({map_type(item) for item in value_type})
        return " | ".join(types) if types else "Any"
    return map_type(value_type)


def map_type(value_type: Any) -> str:
    if value_type == "integer":
        return "int"
    if value_type == "number":
        return "float"
    if value_type == "boolean":
        return "bool"
    if value_type == "string":
        return "str"
    if value_type == "array":
        return "list[Any]"
    if value_type == "object":
        return "dict[str, Any]"
    return "Any"


def field_line(param: dict[str, Any]) -> str:
    raw_name = str(param["name"])
    py_name = snake(raw_name)
    ann = annotation(param)
    default = "..." if param.get("required") else "None"
    if default == "None":
        ann = f"{ann} | None"
    if py_name != raw_name:
        return f"    {py_name}: {ann} = Field(default={default}, alias={raw_name!r})"
    return f"    {py_name}: {ann} = {default}"


def method_func_line(method: dict[str, Any]) -> tuple[str, str]:
    api_name = str(method["name"])
    if "." in api_name:
        group, raw_method = api_name.split(".", 1)
    else:
        group, raw_method = "api", api_name
    method_name = snake(raw_method)
    cls_name = pascal(api_name)
    signature = f"    async def {method_name}(self, **params: Any) -> Any:"
    body = f"        return await self._bot({cls_name}(**params))"
    return group, f"{signature}\n{body}"


def main() -> None:
    tree = fetch_json(TREE_URL)["tree"]
    paths = sorted(
        item["path"]
        for item in tree
        if item["type"] == "blob" and item["path"].endswith("/methods.json")
    )

    methods: list[dict[str, Any]] = []
    for path in paths:
        data = fetch_json(f"{BASE_URL}/{path}")
        methods.extend(data.get("methods", []))

    methods.sort(key=lambda item: item["name"])
    groups: dict[str, list[str]] = {}

    lines: list[str] = [
        "from __future__ import annotations",
        "",
        "from typing import Any",
        "",
        "from pydantic import Field",
        "",
        "from vkapi.methods.base import VKMethod",
        "",
        "",
        "class MethodNamespace:",
        "    def __init__(self, bot: Any) -> None:",
        "        self._bot = bot",
        "",
        "",
    ]

    exported: list[str] = ["METHOD_GROUPS", "MethodNamespace"]
    for method in methods:
        api_name = str(method["name"])
        class_name = pascal(api_name)
        exported.append(class_name)
        lines.extend(
            [
                f"class {class_name}(VKMethod[Any]):",
                f"    __api_method__ = {api_name!r}",
            ],
        )
        params = method.get("parameters") or []
        if params:
            lines.extend(field_line(param) for param in params)
        else:
            lines.append("    pass")
        lines.append("")
        group, func = method_func_line(method)
        groups.setdefault(group, []).append(func)

    for group_name, funcs in sorted(groups.items()):
        namespace_name = f"{pascal(group_name)}Methods"
        exported.append(namespace_name)
        lines.append(f"class {namespace_name}(MethodNamespace):")
        for func in funcs:
            lines.append(func)
            lines.append("")
        if not funcs:
            lines.append("    pass")
        lines.append("")

    lines.append("METHOD_GROUPS: dict[str, type[MethodNamespace]] = {")
    lines.extend(
        f"    {group_name!r}: {pascal(group_name)}Methods,"
        for group_name in sorted(groups)
    )
    lines.append("}")
    lines.append("")
    lines.append("__all__ = [")
    lines.extend(f"    {name!r}," for name in exported)
    lines.append("]")
    lines.append("")

    OUT.write_text("\n".join(lines), encoding="utf-8")
    print(f"Generated {len(methods)} VK API methods into {OUT}")


if __name__ == "__main__":
    main()
