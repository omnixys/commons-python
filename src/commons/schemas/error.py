from __future__ import annotations

from typing import Any

from pydantic import BaseModel, ConfigDict


class ErrorSchema(BaseModel):
    model_config = ConfigDict(extra="allow")
    code: str
    message: str
    details: dict[str, Any] | None = None
    error_id: str | None = None


class ErrorResponseSchema(BaseModel):
    error: ErrorSchema
