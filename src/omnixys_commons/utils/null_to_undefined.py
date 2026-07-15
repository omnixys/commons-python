from __future__ import annotations

from typing import Any

SENTINEL = "__OMNIXYS_UNDEFINED__"


def null_to_undefined(data: dict[str, Any] | None) -> dict[str, Any] | None:
    if data is None:
        return data
    return {k: v if v is not None else SENTINEL for k, v in data.items()}


def undefined_to_null(data: dict[str, Any] | None) -> dict[str, Any] | None:
    if data is None:
        return data
    return {k: v if v != SENTINEL else None for k, v in data.items()}
