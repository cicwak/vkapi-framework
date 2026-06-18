from __future__ import annotations

from collections.abc import Awaitable, Callable
from typing import Any, Protocol


class Middleware(Protocol):
    async def __call__(
        self,
        handler: Callable[[Any, dict[str, Any]], Awaitable[Any]],
        event: Any,
        data: dict[str, Any],
    ) -> Any: ...


class MiddlewareManager:
    def __init__(self) -> None:
        self._middlewares: list[Middleware] = []

    def register(self, middleware: Middleware) -> Middleware:
        self._middlewares.append(middleware)
        return middleware

    def __call__(self, middleware: Middleware) -> Middleware:
        return self.register(middleware)

    def __iter__(self):
        return iter(self._middlewares)

    def wrap(
        self,
        middlewares: list[Middleware],
        handler: Callable[[Any, dict[str, Any]], Awaitable[Any]],
    ) -> Callable[[Any, dict[str, Any]], Awaitable[Any]]:
        wrapped = handler
        for middleware in reversed(middlewares):
            current = wrapped

            async def call(
                event: Any,
                data: dict[str, Any],
                mw: Middleware = middleware,
                nxt=current,
            ) -> Any:
                return await mw(nxt, event, data)

            wrapped = call
        return wrapped
