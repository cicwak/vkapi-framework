from __future__ import annotations

from collections.abc import Callable
from dataclasses import dataclass, field
from typing import Any, cast

from vkapi.dependency import maybe_await, resolve_dependencies

from .bases import FilterResult

CallbackType = Callable[..., Any]


@dataclass
class HandlerObject:
    callback: CallbackType
    filters: list[CallbackType] = field(default_factory=list)
    flags: dict[str, Any] = field(default_factory=dict)

    async def check(self, event: Any, **kwargs: Any) -> tuple[bool, dict[str, Any]]:
        data: dict[str, Any] = {}
        for filter_ in self.filters:
            result = await self._call_filter(filter_, event, {**kwargs, **data})
            if not result:
                return False, {}
            if isinstance(result, dict):
                data.update(result)
        return True, data

    async def _call_filter(
        self,
        filter_: CallbackType,
        event: Any,
        data: dict[str, Any],
    ) -> FilterResult:
        callback = filter_
        kwargs = await resolve_dependencies(callback, event=event, data=data, cache={})
        kwargs.pop("event", None)
        result = await maybe_await(callback(event, **kwargs))
        return cast(FilterResult, result)

    async def call(self, event: Any, data: dict[str, Any]) -> Any:
        cache = data.setdefault("_dependency_cache", {})
        kwargs = await resolve_dependencies(self.callback, event=event, data=data, cache=cache)
        return await maybe_await(self.callback(**kwargs))
