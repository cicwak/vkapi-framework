from __future__ import annotations

from enum import StrEnum


class FSMStrategy(StrEnum):
    USER_IN_PEER = "user_in_peer"
    USER = "user"
    PEER = "peer"
