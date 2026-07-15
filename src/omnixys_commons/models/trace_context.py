from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field

from omnixys_commons.enums.log_level import LogLevel


class TraceContext(BaseModel):
    model_config = ConfigDict(extra="allow")

    trace_id: str | None = Field(default=None, alias="traceId")
    span_id: str | None = Field(default=None, alias="spanId")
    parent_span_id: str | None = Field(default=None, alias="parentSpanId")
    sampled: str | None = None

    def is_valid(self) -> bool:
        return self.trace_id is not None and self.span_id is not None


class LogEntry(BaseModel):
    model_config = ConfigDict(extra="allow")

    level: LogLevel
    message: str
    service: str | None = None
    timestamp: str | None = None
    metadata: dict[str, object] | None = None
    trace_context: TraceContext | None = Field(default=None, alias="traceContext")
    operation: str | None = None
