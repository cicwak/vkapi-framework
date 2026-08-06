from __future__ import annotations

from typing import Any

from .context import FSMContext
from .state import State, StatesGroup, state_to_str


class StateFilter:
    def __init__(self, *states: State | str | None | type[StatesGroup]) -> None:
        self.states = states
        self._allowed_states = self._resolve_states(states)

    async def __call__(
        self,
        event: Any,
        state: FSMContext | None = None,
        raw_state: str | None = None,
        **kwargs: Any,
    ) -> bool:
        current_state = raw_state
        if current_state is None and state is not None:
            current_state = await state.get_state()
        return current_state in self._allowed_states

    def _resolve_states(
        self,
        states: tuple[State | str | None | type[StatesGroup], ...],
    ) -> set[str | None]:
        allowed: set[str | None] = set()
        for state in states:
            if isinstance(state, type):
                group_states: tuple[State, ...] = state.__states__  # pyrefly: ignore [missing-attribute]
                allowed.update(item.state for item in group_states)
                continue
            allowed.add(state_to_str(state))
        return allowed
