"""Small helper utilities used by the bot."""

from __future__ import annotations

from typing import Any


def safe_get(mapping: dict[str, Any], key: str, default: Any = None) -> Any:
    try:
        return mapping.get(key, default)
    except Exception:
        return default
