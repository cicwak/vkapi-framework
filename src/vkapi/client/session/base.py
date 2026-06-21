from __future__ import annotations

import abc
import json
from collections.abc import AsyncGenerator, Awaitable, Callable
from typing import TYPE_CHECKING, Any, TypeVar, cast

from vkapi.exceptions import VKDecodeError, make_api_error

if TYPE_CHECKING:
    from vkapi.client.bot import Bot
    from vkapi.methods.base import MethodT

T = TypeVar("T")
RequestHandler = Callable[["Bot", "MethodT[Any]", float | None], Awaitable[Any]]
RequestMiddleware = Callable[[RequestHandler], RequestHandler]


class RequestMiddlewareManager:
    def __init__(self) -> None:
        self._middlewares: list[RequestMiddleware] = []

    def register(self, middleware: RequestMiddleware) -> RequestMiddleware:
        self._middlewares.append(middleware)
        return middleware

    def wrap(self, handler: RequestHandler) -> RequestHandler:
        wrapped = handler
        for middleware in reversed(self._middlewares):
            wrapped = middleware(wrapped)
        return wrapped


class BaseSession(abc.ABC):
    def __init__(
        self,
        *,
        api_url: str = "https://api.vk.com/method/{method}",
        timeout: float = 60.0,
        json_loads: Callable[[str], Any] = json.loads,
        json_dumps: Callable[[Any], str] = json.dumps,
    ) -> None:
        self.api_url = api_url
        self.timeout = timeout
        self.json_loads = json_loads
        self.json_dumps = json_dumps
        self.middleware = RequestMiddlewareManager()

    def build_url(self, method: str) -> str:
        return self.api_url.format(method=method)

    def check_response(self, method: str, content: str) -> Any:
        try:
            payload = self.json_loads(content)
        except Exception as exc:  # noqa: BLE001
            raise VKDecodeError("Failed to decode VK API response", content) from exc

        if not isinstance(payload, dict):
            raise VKDecodeError("VK API response must be an object", payload)
        payload = cast(dict[str, Any], payload)

        if "error" in payload:
            error = payload["error"]
            if isinstance(error, dict):
                raise make_api_error(method, cast(dict[str, Any], error))
            raise VKDecodeError("VK API error payload must be an object", payload)

        if "response" not in payload:
            raise VKDecodeError("VK API response does not contain `response`", payload)

        return payload["response"]

    def prepare_value(self, value: Any) -> str | int | float | None:
        if value is None:
            return None
        if isinstance(value, bool):
            return 1 if value else 0
        if isinstance(value, int | float | str):
            return value
        if hasattr(value, "model_dump"):
            return self.json_dumps(value.model_dump(mode="json", exclude_none=True))
        if isinstance(value, dict | list | tuple):
            return self.json_dumps(value)
        return str(value)

    def prepare_params(self, bot: Bot, method: MethodT[Any]) -> dict[str, Any]:
        params: dict[str, Any] = {
            "access_token": bot.token,
            "v": bot.api_version,
        }
        for key, value in method.build_request().items():
            prepared = self.prepare_value(value)
            if prepared is not None:
                params[key] = prepared
        return params

    @abc.abstractmethod
    async def close(self) -> None:
        """Close underlying resources."""

    @abc.abstractmethod
    async def make_request(
        self,
        bot: Bot,
        method: MethodT[T],
        timeout: float | None = None,
    ) -> T:
        """Make one VK API request."""

    @abc.abstractmethod
    async def stream_content(
        self,
        url: str,
        *,
        timeout: float = 30.0,
        chunk_size: int = 65536,
    ) -> AsyncGenerator[bytes, None]:
        yield b""

    async def __call__(
        self,
        bot: Bot,
        method: MethodT[T],
        timeout: float | None = None,
    ) -> T:
        wrapped = self.middleware.wrap(cast(RequestHandler, self.make_request))
        return cast(T, await wrapped(bot, method, timeout))

    async def __aenter__(self) -> BaseSession:
        return self

    async def __aexit__(self, *_: Any) -> None:
        await self.close()
