from __future__ import annotations

import re

from pydantic import BaseModel, ConfigDict, Field, field_validator

_TRACE_ID_RE = re.compile(r"^[a-f0-9]{32}$", re.IGNORECASE)
_SEMVER_RE = re.compile(r"^\d+\.\d+$")


class ContractMetadataSchema(BaseModel):
    model_config = ConfigDict(extra="forbid")

    request_id: str = Field(alias="requestId", min_length=1, max_length=128)
    correlation_id: str = Field(alias="correlationId", min_length=1, max_length=128)
    trace_id: str | None = Field(default=None, alias="traceId")
    actor_id: str | None = Field(default=None, alias="actorId")
    tenant_id: str | None = Field(default=None, alias="tenantId")

    @field_validator("trace_id")
    @classmethod
    def trace_must_be_hex32(cls, v: str | None) -> str | None:
        if v is not None and not _TRACE_ID_RE.match(v):
            raise ValueError("traceId must be a 32-character hex string")
        return v


class ContractEnvelope[T](BaseModel):
    model_config = ConfigDict(extra="forbid")

    schema_version: str = Field(alias="schemaVersion")
    occurred_at: str = Field(alias="occurredAt")
    metadata: ContractMetadataSchema
    payload: T

    @field_validator("schema_version")
    @classmethod
    def schema_version_must_be_semver(cls, v: str) -> str:
        if not _SEMVER_RE.match(v):
            raise ValueError("schemaVersion must match semver format MAJOR.MINOR")
        return v
