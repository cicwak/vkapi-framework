from __future__ import annotations

import asyncio
import time


class AsyncRateLimiter:
    """Small token-bucket limiter for VK API calls."""

    def __init__(self, rate: float | None = None, per: float = 1.0) -> None:
        self.rate = rate
        self.per = per
        self._lock = asyncio.Lock()
        self._tokens = float(rate or 0)
        self._updated_at = time.monotonic()

    async def acquire(self) -> None:
        if not self.rate:
            return
        async with self._lock:
            while True:
                now = time.monotonic()
                elapsed = now - self._updated_at
                self._updated_at = now
                self._tokens = min(float(self.rate), self._tokens + elapsed * self.rate / self.per)
                if self._tokens >= 1:
                    self._tokens -= 1
                    return
                missing = 1 - self._tokens
                await asyncio.sleep(missing * self.per / self.rate)
