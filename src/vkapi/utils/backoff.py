from __future__ import annotations

import asyncio
from dataclasses import dataclass
from random import random


@dataclass
class BackoffConfig:
    min_delay: float = 1.0
    max_delay: float = 5.0
    factor: float = 1.3
    jitter: float = 0.1


class Backoff:
    def __init__(self, config: BackoffConfig | None = None) -> None:
        self.config = config or BackoffConfig()
        self.counter = 0
        self.next_delay = self.config.min_delay

    def reset(self) -> None:
        self.counter = 0
        self.next_delay = self.config.min_delay

    async def asleep(self) -> None:
        delay = self.next_delay + random() * self.config.jitter
        self.counter += 1
        self.next_delay = min(self.config.max_delay, self.next_delay * self.config.factor)
        await asyncio.sleep(delay)
