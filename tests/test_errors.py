"""Behavioral tests for the commons error layer."""

from __future__ import annotations

import pytest

from commons.errors import (
    ErrorCode,
    EventNotFoundException,
    ExceptionContext,
    OmnixysException,
    TicketNotFoundException,
    UserNotFoundException,
    is_error_code,
    with_metadata,
)
from commons.errors.error_code import ERROR_CODES


def test_error_code_is_string_enum() -> None:
    assert ErrorCode.USER_NOT_FOUND.value == "USER_NOT_FOUND"
    assert str(ErrorCode.FORBIDDEN) == "FORBIDDEN"
    assert len(ERROR_CODES) >= 100
    assert all(isinstance(code, ErrorCode) for code in ERROR_CODES)


def test_is_error_code() -> None:
    assert is_error_code("EVENT_NOT_FOUND") is True
    assert is_error_code("NOT_A_REAL_CODE") is False
    assert is_error_code(ErrorCode.SEAT_OCCUPIED) is True


def test_omnixys_exception_carries_code_and_message() -> None:
    exc = OmnixysException(ErrorCode.EVENT_CLOSED, "Event is closed")
    assert exc.code == ErrorCode.EVENT_CLOSED
    assert str(exc) == "Event is closed"
    assert exc.args == ("Event is closed",)
    assert exc.context == ExceptionContext()
    assert exc.metadata == {}


def test_omnixys_exception_context_metadata() -> None:
    context = ExceptionContext(request_id="req-1", tenant_id="tenant-1")
    exc = OmnixysException(
        ErrorCode.ACCESS_DENIED,
        "denied",
        context=context,
        metadata={"key": "value"},
    )
    assert exc.request_id == "req-1"
    assert exc.tenant_id == "tenant-1"
    assert exc.correlation_id is None
    assert exc.metadata == {"key": "value"}
    assert exc.metadata is not context


def test_omnixys_exception_chains_cause() -> None:
    cause = ValueError("boom")
    exc = OmnixysException(ErrorCode.INTERNAL_SERVER_ERROR, "failed", cause=cause)
    assert exc.__cause__ is cause


def test_domain_exceptions_set_code_and_message() -> None:
    assert EventNotFoundException().code == ErrorCode.EVENT_NOT_FOUND
    assert UserNotFoundException().code == ErrorCode.USER_NOT_FOUND
    assert TicketNotFoundException().code == ErrorCode.TICKET_NOT_FOUND
    assert "not found" in str(EventNotFoundException()).lower()


def test_domain_exceptions_accept_context_kwargs() -> None:
    context = ExceptionContext(actor_id="user-1")
    exc = EventNotFoundException(context=context)
    assert exc.actor_id == "user-1"


def test_with_metadata_merges() -> None:
    merged = with_metadata({"a": 1}, {"b": 2})
    assert merged == {"a": 1, "b": 2}
    assert with_metadata(None, {"b": 2}) == {"b": 2}


def test_exception_is_raisable_and_catchable() -> None:
    with pytest.raises(OmnixysException) as excinfo:
        raise EventNotFoundException()
    assert excinfo.value.code == ErrorCode.EVENT_NOT_FOUND
