from __future__ import annotations

import inspect
from collections.abc import Callable
from typing import Any, TypeVar, get_args, get_origin, get_type_hints

T = TypeVar("T")


class Depends:
    def __init__(self, dependency: Callable[..., T], *, use_cache: bool = True) -> None:
        self.dependency = dependency
        self.use_cache = use_cache
        self.cache_key = f"dep:{id(dependency)}"


async def maybe_await(value: Any) -> Any:
    if inspect.isawaitable(value):
        return await value
    return value


def _matches_annotation(value: Any, annotation: Any) -> bool:
    if annotation is inspect.Parameter.empty:
        return False
    origin = get_origin(annotation)
    if origin is not None:
        return any(_matches_annotation(value, item) for item in get_args(annotation))
    try:
        return isinstance(value, annotation)
    except TypeError:
        return False


async def resolve_dependencies(
    callback: Callable[..., Any],
    *,
    event: Any,
    data: dict[str, Any],
    cache: dict[str, Any],
) -> dict[str, Any]:
    signature = inspect.signature(callback)
    try:
        type_hints = get_type_hints(callback)
    except Exception:  # noqa: BLE001
        type_hints = {}
    resolved: dict[str, Any] = {}
    for name, parameter in signature.parameters.items():
        if name in data:
            resolved[name] = data[name]
            continue
        default = parameter.default
        if isinstance(default, Depends):
            if default.use_cache and default.cache_key in cache:
                resolved[name] = cache[default.cache_key]
                continue
            dep_kwargs = await resolve_dependencies(
                default.dependency,
                event=event,
                data=data,
                cache=cache,
            )
            value = await maybe_await(default.dependency(**dep_kwargs))
            if default.use_cache:
                cache[default.cache_key] = value
            resolved[name] = value
            continue
        annotation = type_hints.get(name, parameter.annotation)
        if _matches_annotation(event, annotation):
            resolved[name] = event
            continue
        for value in data.values():
            if _matches_annotation(value, annotation):
                resolved[name] = value
                break
        if name not in resolved and name in {"event", "message", "update"}:
            resolved[name] = event
    return resolved
