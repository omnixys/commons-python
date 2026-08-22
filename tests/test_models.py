"""Behavioral tests for commons models."""

from __future__ import annotations

from commons.enums.sort_direction import SortDirection
from commons.models import (
    ApiResponse,
    ContractEnvelope,
    ContractMetadata,
    PaginationResponse,
    SortCriteria,
)
from commons.models.pagination import PaginationRequest


def test_sort_criteria_model() -> None:
    criteria = SortCriteria(field="name")
    assert criteria.direction == SortDirection.ASC
    desc = SortCriteria(field="name", direction=SortDirection.DESC)
    assert desc.direction == SortDirection.DESC


def test_pagination_request_defaults() -> None:
    req = PaginationRequest()
    assert req.page == 0
    assert req.size == 20
    assert req.sort == ()
    assert PaginationRequest(page=2, size=50) == PaginationRequest(2, 50)


def test_pagination_response_total_pages() -> None:
    resp = PaginationResponse(items=[1, 2, 3], total=25, page=0, size=10)
    assert resp.total_pages == 3
    assert resp.has_next is True
    assert resp.has_previous is False


def test_pagination_response_last_page() -> None:
    resp = PaginationResponse(total=10, page=1, size=10)
    assert resp.total_pages == 1
    assert resp.has_next is False
    assert resp.has_previous is True


def test_pagination_response_zero_size() -> None:
    resp = PaginationResponse(total=10, page=0, size=0)
    assert resp.total_pages == 0
    assert resp.has_next is False


def test_api_response_ok() -> None:
    resp = ApiResponse.ok({"id": 1})
    assert resp.success is True
    assert resp.data == {"id": 1}
    assert resp.errors == []


def test_api_response_error() -> None:
    resp = ApiResponse.error("something failed")
    assert resp.success is False
    assert resp.message == "something failed"
    assert resp.data is None


def test_contract_envelope_populate_and_dump() -> None:
    env = ContractEnvelope(
        schemaVersion="1.0",
        occurredAt="2026-08-06T10:00:00Z",
        metadata=ContractMetadata(requestId="req", correlationId="corr"),
        payload={"hello": "world"},
    )
    dumped = env.model_dump(by_alias=True)
    assert dumped["schemaVersion"] == "1.0"
    assert dumped["metadata"]["requestId"] == "req"
    assert dumped["payload"] == {"hello": "world"}
    assert env.schema_version == "1.0"
