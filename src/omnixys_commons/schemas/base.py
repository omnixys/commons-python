from __future__ import annotations

from datetime import datetime
from typing import Any

from pydantic import BaseModel, ConfigDict


class AuditSchema(BaseModel):
    created_by: str | None = None
    updated_by: str | None = None
    created_at: datetime | None = None
    updated_at: datetime | None = None


class BaseSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True, extra="allow")
    id: str
    status: str | None = None
    audit: AuditSchema | None = None


class BaseResponseSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True, extra="allow")
    success: bool = True
    message: str | None = None
    errors: list[dict[str, Any]] | None = None
    data: Any | None = None
