from __future__ import annotations

from typing import Any

from .base import Filter


class Command(Filter):
    def __init__(
        self,
        *commands: str,
        prefixes: str | tuple[str, ...] = "/",
        ignore_case: bool = True,
    ) -> None:
        self.commands = {command.lower() if ignore_case else command for command in commands}
        self.prefixes = (prefixes,) if isinstance(prefixes, str) else prefixes
        self.ignore_case = ignore_case

    async def __call__(self, event: Any, **kwargs: Any) -> bool | dict[str, Any]:
        text = getattr(event, "text", "") or ""
        for prefix in self.prefixes:
            if not text.startswith(prefix):
                continue
            body = text[len(prefix) :].strip()
            if not body:
                continue
            command, _, args = body.partition(" ")
            lookup = command.lower() if self.ignore_case else command
            if lookup in self.commands:
                return {"command": command, "command_args": args}
        return False
