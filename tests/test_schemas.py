"""Behavioral tests for commons schemas and the contract schema registry."""

from __future__ import annotations

import uuid

import pytest
from pydantic import BaseModel, ConfigDict, ValidationError

from commons.schemas import (
    ActorIdModel,
    ContractEnvelope,
    ContractMetadataSchema,
    ContractSchemaNotFoundError,
    ContractSchemaRegistry,
    UserIdModel,
    validate_uuid4,
)


class SampleContract(BaseModel):
    model_config = ConfigDict(extra="forbid")
    name: str


def test_validate_uuid4_normalizes() -> None:
    raw = str(uuid.uuid4())
    assert validate_uuid4(raw.upper()) == raw


def test_validate_uuid4_rejects_invalid() -> None:
    with pytest.raises(ValueError):
        validate_uuid4("not-a-uuid")


def test_id_models_accept_alias() -> None:
    model = ActorIdModel.model_validate({"actorId": str(uuid.uuid4())})
    assert model.actor_id
    assert model.model_dump(by_alias=True)["actorId"] == model.actor_id


def test_id_models_reject_bad_uuid() -> None:
    with pytest.raises(ValidationError):
        UserIdModel.model_validate({"userId": "nope"})


def test_id_models_reject_extra_fields() -> None:
    with pytest.raises(ValidationError):
        ActorIdModel.model_validate({"actorId": str(uuid.uuid4()), "extra": 1})


def test_contract_metadata_trace_id_hex32() -> None:
    metadata = ContractMetadataSchema(
        requestId="req",
        correlationId="corr",
        traceId="a" * 32,
    )
    assert metadata.trace_id == "a" * 32
    with pytest.raises(ValidationError):
        ContractMetadataSchema(
            requestId="req",
            correlationId="corr",
            traceId="short",
        )


def test_contract_envelope_validates_semver() -> None:
    env = ContractEnvelope(
        schemaVersion="2.1",
        occurredAt="2026-08-06T10:00:00Z",
        metadata=ContractMetadataSchema(requestId="r", correlationId="c"),
        payload={},
    )
    assert env.schema_version == "2.1"
    with pytest.raises(ValidationError):
        ContractEnvelope(
            schemaVersion="1.0.0",
            occurredAt="2026-08-06T10:00:00Z",
            metadata=ContractMetadataSchema(requestId="r", correlationId="c"),
            payload={},
        )


def test_registry_register_and_parse() -> None:
    registry = ContractSchemaRegistry()
    registry.register("user", "1.0", SampleContract)
    assert registry.has("user", "1.0") is True
    parsed = registry.parse("user", "1.0", {"name": "Ada"})
    assert isinstance(parsed, SampleContract)
    assert parsed.name == "Ada"


def test_registry_unknown_contract_raises() -> None:
    registry = ContractSchemaRegistry()
    with pytest.raises(ContractSchemaNotFoundError):
        registry.parse("user", "1.0", {"name": "Ada"})


def test_registry_diagnostics() -> None:
    registry = ContractSchemaRegistry()
    registry.register("b", "1.0", SampleContract)
    registry.register("a", "2.0", SampleContract)
    assert registry.diagnostics()["schemas"] == ["a@2.0", "b@1.0"]
