from __future__ import annotations

from typing import Any


class Filter:
    async def __call__(self, event: Any, **kwargs: Any) -> bool | dict[str, Any]:
        return True

    def __and__(self, other: Any) -> AndFilter:
        return AndFilter(self, other)

    def __or__(self, other: Any) -> OrFilter:
        return OrFilter(self, other)

    def __invert__(self) -> InvertFilter:
        return InvertFilter(self)


class AndFilter(Filter):
    def __init__(self, *filters: Any) -> None:
        self.filters = filters

    async def __call__(self, event: Any, **kwargs: Any) -> bool:
        for filter_ in self.filters:
            if not await _call_filter(filter_, event, kwargs):
                return False
        return True


class OrFilter(Filter):
    def __init__(self, *filters: Any) -> None:
        self.filters = filters

    async def __call__(self, event: Any, **kwargs: Any) -> bool:
        for filter_ in self.filters:
            if await _call_filter(filter_, event, kwargs):
                return True
        return False


class InvertFilter(Filter):
    def __init__(self, filter_: Any) -> None:
        self.filter = filter_

    async def __call__(self, event: Any, **kwargs: Any) -> bool:
        return not await _call_filter(self.filter, event, kwargs)


async def _call_filter(filter_: Any, event: Any, kwargs: dict[str, Any]) -> bool:
    result = filter_(event, **kwargs)
    if hasattr(result, "__await__"):
        result = await result
    return bool(result)
