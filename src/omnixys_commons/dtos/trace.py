from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field


class TraceContextDTO(BaseModel):
    model_config = ConfigDict(extra="allow")
    trace_id: str | None = Field(default=None, alias="traceId")
    span_id: str | None = Field(default=None, alias="spanId")
    parent_span_id: str | None = Field(default=None, alias="parentSpanId")
    sampled: str | None = None


class BuildKafkaHeaderDTO(BaseModel):
    model_config = ConfigDict(extra="allow")
    topic: str
    operation: str
    trace: TraceContextDTO | None = None
    version: str
    service: str
