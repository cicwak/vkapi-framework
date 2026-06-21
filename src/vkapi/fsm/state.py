from __future__ import annotations

from typing import Any, cast


class State:
    def __init__(self, state: str | None = None) -> None:
        self._state = state
        self._group_name: str | None = None
        self._attr_name: str | None = None

    def bind(self, group_name: str, attr_name: str) -> None:
        self._group_name = group_name
        self._attr_name = attr_name
        if self._state is None:
            self._state = attr_name

    @property
    def state(self) -> str:
        if self._state is None:
            raise RuntimeError("State is not bound to a StatesGroup")
        if self._group_name is None:
            return self._state
        return f"{self._group_name}:{self._state}"

    def __str__(self) -> str:
        return self.state

    def __repr__(self) -> str:
        return f"State({self.state!r})"


class StatesGroupMeta(type):
    def __new__(
        mcls,
        name: str,
        bases: tuple[type[Any], ...],
        namespace: dict[str, Any],
        **kwargs: Any,
    ) -> StatesGroupMeta:
        cls = super().__new__(mcls, name, bases, namespace, **kwargs)
        group_name = str(namespace.get("__state_group_name__", name))
        states: list[State] = []
        for base in bases:
            states.extend(getattr(base, "__states__", ()))
        for attr_name, value in cls.__dict__.items():
            if isinstance(value, State):
                value.bind(group_name, attr_name)
                states.append(value)
        cls_any = cast(Any, cls)
        cls_any.__state_group_name__ = group_name
        cls_any.__states__ = tuple(states)
        return cls


class StatesGroup(metaclass=StatesGroupMeta):
    __state_group_name__: str
    __states__: tuple[State, ...]


def state_to_str(state: State | str | None | type[StatesGroup]) -> str | None:
    if state is None:
        return None
    if isinstance(state, State):
        return state.state
    if isinstance(state, str):
        return state
    raise TypeError("StatesGroup classes cannot be converted to a single state")
