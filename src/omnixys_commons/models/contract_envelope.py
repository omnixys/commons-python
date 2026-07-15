from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field


class ContractMetadata(BaseModel):
    model_config = ConfigDict(extra="allow")

    request_id: str | None = Field(default=None, alias="requestId")
    correlation_id: str | None = Field(default=None, alias="correlationId")
    trace_id: str | None = Field(default=None, alias="traceId")
    actor_id: str | None = Field(default=None, alias="actorId")
    tenant_id: str | None = Field(default=None, alias="tenantId")


class ContractEnvelope[T](BaseModel):
    model_config = ConfigDict(extra="allow")

    schema_version: str = Field(alias="schemaVersion")
    occurred_at: str = Field(alias="occurredAt")
    metadata: ContractMetadata
    payload: T
