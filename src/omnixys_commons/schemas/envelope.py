from __future__ import annotations

from typing import Any

from pydantic import BaseModel, ConfigDict


class EnvelopeSchema(BaseModel):
    model_config = ConfigDict(extra="allow")
    id: str
    type: str
    source: str
    spec_version: str = "1.0"
    data_content_type: str = "application/json"
    data: dict[str, Any]
    time: str | None = None
    correlation_id: str | None = None
