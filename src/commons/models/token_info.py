from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class TokenInfo:
    token: str
    expires_at: str | None = None
    token_type: str | None = None
