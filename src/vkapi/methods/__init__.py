from .base import RawMethod, VKMethod

try:
    from .generated import *  # noqa: F403
    from .generated import __all__ as _generated_all
except ImportError:  # pragma: no cover - generated file is created by scripts/update_schema.py
    _generated_all = []

__all__ = ["RawMethod", "VKMethod", *_generated_all]
