from __future__ import annotations

from pydantic import BaseModel


class HealthSchema(BaseModel):
    status: str = "UP"
    service: str
    version: str | None = None
    timestamp: str | None = None
