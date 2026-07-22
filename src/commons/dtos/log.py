from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field

from commons.enums.log_level import LogLevel
from commons.models.trace_context import TraceContext


class LogDTO(BaseModel):
    model_config = ConfigDict(extra="allow")
    level: LogLevel
    message: str
    service: str
    timestamp: str
    metadata: dict[str, object] | None = None
    trace_context: TraceContext | None = Field(default=None, alias="traceContext")
    operation: str | None = None


class ContextLogDTO(BaseModel):
    model_config = ConfigDict(extra="allow")
    log: LogDTO
    ctx: object | None = None
