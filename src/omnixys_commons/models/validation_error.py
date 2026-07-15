from __future__ import annotations

from pydantic import BaseModel, ConfigDict


class ValidationError(BaseModel):
    model_config = ConfigDict(extra="allow")

    field: str | None = None
    message: str
    code: str | None = None
