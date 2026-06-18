from __future__ import annotations

from typing import Any, Final

UNHANDLED: Final = object()
REJECTED: Final = object()


class SkipHandler(Exception):
    pass


FilterResult = bool | dict[str, Any]
