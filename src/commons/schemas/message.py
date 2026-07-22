from __future__ import annotations

from typing import Any

from pydantic import BaseModel, ConfigDict


class EventMessageSchema(BaseModel):
    model_config = ConfigDict(extra="allow")
    event_type: str
    source: str
    data: dict[str, Any]


class RetryableMessageSchema(BaseModel):
    model_config = ConfigDict(extra="allow")
    message: EventMessageSchema
    retry_count: int = 0
    max_retries: int = 3
    last_error: str | None = None
