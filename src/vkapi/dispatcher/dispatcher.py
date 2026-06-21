from __future__ import annotations

import asyncio
import contextlib
import signal
from collections.abc import AsyncGenerator, Awaitable
from typing import Any

from aiohttp import ClientError, ClientSession, ClientTimeout

from vkapi.client.bot import Bot
from vkapi.dispatcher.event.bases import UNHANDLED
from vkapi.fsm import BaseStorage, FSMStrategy, MemoryStorage
from vkapi.fsm.middleware import FSMMiddleware
from vkapi.types import Update
from vkapi.utils.backoff import Backoff, BackoffConfig

from .router import Router


class Dispatcher(Router):
    def __init__(
        self,
        *,
        name: str | None = None,
        storage: BaseStorage | None = None,
        fsm_strategy: FSMStrategy = FSMStrategy.USER_IN_PEER,
        **workflow_data: Any,
    ) -> None:
        super().__init__(name=name)
        self.workflow_data = workflow_data
        self.storage = storage if storage is not None else MemoryStorage()
        self.fsm_strategy = fsm_strategy
        self._running_lock = asyncio.Lock()
        self._stop_signal: asyncio.Event | None = None
        self._handle_update_tasks: set[asyncio.Task[Any]] = set()
        fsm_middleware = FSMMiddleware(self.storage, self.fsm_strategy)
        for observer in self.observers.values():
            observer.outer_middleware(fsm_middleware)

    async def feed_update(self, bot: Bot, update: Update | dict[str, Any], **kwargs: Any) -> Any:
        if not isinstance(update, Update):
            update = Update.model_validate(update)
        update.as_(bot)
        event = update.event
        return await self.propagate_event(
            update.event_type,
            event,
            bot=bot,
            dispatcher=self,
            event_update=update,
            event_router=self,
            **self.workflow_data,
            **kwargs,
        )

    async def _process_update(self, bot: Bot, update: Update, **kwargs: Any) -> bool:
        try:
            response = await self.feed_update(bot, update, **kwargs)
            return response is not UNHANDLED
        except Exception as exc:  # noqa: BLE001
            error_observer = self.observers.get("error")
            if error_observer:
                await self.propagate_event(
                    "error",
                    update,
                    bot=bot,
                    dispatcher=self,
                    exception=exc,
                    event_update=update,
                )
            return True

    async def _listen_updates(
        self,
        bot: Bot,
        *,
        polling_timeout: int = 25,
        backoff_config: BackoffConfig | None = None,
    ) -> AsyncGenerator[Update, None]:
        server_data = await bot.get_long_poll_server()
        server = str(server_data["server"])
        key = str(server_data["key"])
        ts = str(server_data["ts"])
        backoff = Backoff(backoff_config)
        async with ClientSession() as session:
            while True:
                try:
                    async with session.get(
                        server,
                        params={"act": "a_check", "key": key, "ts": ts, "wait": polling_timeout},
                        timeout=ClientTimeout(total=polling_timeout + 10),
                    ) as response:
                        payload = await response.json()
                except (TimeoutError, ClientError):
                    await backoff.asleep()
                    continue

                backoff.reset()
                failed = payload.get("failed")
                if failed == 1:
                    ts = str(payload["ts"])
                    continue
                if failed in {2, 3}:
                    server_data = await bot.get_long_poll_server()
                    server = str(server_data["server"])
                    key = str(server_data["key"])
                    ts = str(server_data["ts"])
                    continue
                if failed:
                    await backoff.asleep()
                    continue

                ts = str(payload.get("ts", ts))
                for raw_update in payload.get("updates", []):
                    yield Update.model_validate(raw_update)

    async def _polling(
        self,
        bot: Bot,
        *,
        polling_timeout: int,
        handle_as_tasks: bool,
        tasks_concurrency_limit: int | None,
        **kwargs: Any,
    ) -> None:
        semaphore = (
            asyncio.Semaphore(tasks_concurrency_limit)
            if tasks_concurrency_limit is not None and handle_as_tasks
            else None
        )
        async for update in self._listen_updates(bot, polling_timeout=polling_timeout):
            coro = self._process_update(bot, update, **kwargs)
            if not handle_as_tasks:
                await coro
                continue
            if semaphore is not None:
                await semaphore.acquire()

                async def limited(handle_update: Awaitable[bool] = coro) -> bool:
                    try:
                        return await handle_update
                    finally:
                        semaphore.release()

                task = asyncio.create_task(limited())
            else:
                task = asyncio.create_task(coro)
            self._handle_update_tasks.add(task)
            task.add_done_callback(self._handle_update_tasks.discard)

    async def start_polling(
        self,
        bot: Bot,
        *,
        polling_timeout: int = 25,
        handle_as_tasks: bool = True,
        handle_signals: bool = True,
        close_bot_session: bool = True,
        tasks_concurrency_limit: int | None = None,
        **kwargs: Any,
    ) -> None:
        async with self._running_lock:
            self._stop_signal = asyncio.Event()
            loop = asyncio.get_running_loop()
            if handle_signals:
                with contextlib.suppress(NotImplementedError):
                    loop.add_signal_handler(signal.SIGINT, self.stop_polling)
                    loop.add_signal_handler(signal.SIGTERM, self.stop_polling)
            polling_task = asyncio.create_task(
                self._polling(
                    bot,
                    polling_timeout=polling_timeout,
                    handle_as_tasks=handle_as_tasks,
                    tasks_concurrency_limit=tasks_concurrency_limit,
                    **kwargs,
                ),
            )
            stop_task = asyncio.create_task(self._stop_signal.wait())
            done, pending = await asyncio.wait(
                {polling_task, stop_task},
                return_when=asyncio.FIRST_COMPLETED,
            )
            for task in pending:
                task.cancel()
                with contextlib.suppress(asyncio.CancelledError):
                    await task
            for task in done:
                task.result()
            if close_bot_session:
                await bot.close()

    def stop_polling(self) -> None:
        if self._stop_signal is not None:
            self._stop_signal.set()

    def run_polling(self, bot: Bot, **kwargs: Any) -> None:
        asyncio.run(self.start_polling(bot, **kwargs))
