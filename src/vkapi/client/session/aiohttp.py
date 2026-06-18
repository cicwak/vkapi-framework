from __future__ import annotations

import asyncio
from collections.abc import AsyncGenerator
from typing import TYPE_CHECKING, Any, TypeVar, cast

from aiohttp import ClientError, ClientSession, ClientTimeout, FormData, TCPConnector

from vkapi.exceptions import VKNetworkError

from .base import BaseSession

if TYPE_CHECKING:
    from vkapi.client.bot import Bot
    from vkapi.methods.base import MethodT

T = TypeVar("T")


class AiohttpSession(BaseSession):
    def __init__(
        self,
        *,
        proxy: str | None = None,
        limit: int = 100,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.proxy = proxy
        self._session: ClientSession | None = None
        self._limit = limit

    async def create_session(self) -> ClientSession:
        if self._session is None or self._session.closed:
            self._session = ClientSession(
                connector=TCPConnector(limit=self._limit, ttl_dns_cache=3600),
            )
        return self._session

    async def close(self) -> None:
        if self._session is not None and not self._session.closed:
            await self._session.close()
            await asyncio.sleep(0.25)

    async def make_request(
        self,
        bot: Bot,
        method: MethodT[T],
        timeout: float | None = None,
    ) -> T:
        session = await self.create_session()
        data = FormData()
        for key, value in self.prepare_params(bot, method).items():
            data.add_field(key, str(value))
        try:
            async with session.post(
                self.build_url(method.__api_method__),
                data=data,
                proxy=self.proxy,
                timeout=ClientTimeout(total=self.timeout if timeout is None else timeout),
            ) as response:
                content = await response.text()
        except TimeoutError as exc:
            raise VKNetworkError(f"Request timeout for {method.__api_method__}") from exc
        except ClientError as exc:
            raise VKNetworkError(f"{type(exc).__name__}: {exc}") from exc

        return cast(T, self.check_response(method.__api_method__, content))

    async def stream_content(
        self,
        url: str,
        *,
        timeout: float = 30.0,
        chunk_size: int = 65536,
    ) -> AsyncGenerator[bytes, None]:
        session = await self.create_session()
        async with session.get(
            url,
            proxy=self.proxy,
            timeout=ClientTimeout(total=timeout),
        ) as response:
            response.raise_for_status()
            async for chunk in response.content.iter_chunked(chunk_size):
                yield chunk
