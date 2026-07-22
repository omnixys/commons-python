from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass(frozen=True, slots=True)
class ExceptionContext:
    request_id: str | None = None
    correlation_id: str | None = None
    trace_id: str | None = None
    actor_id: str | None = None
    tenant_id: str | None = None


class OmnixysException(Exception):  # noqa: N818
    def __init__(
        self,
        code: str,
        message: str,
        *,
        context: ExceptionContext | None = None,
        metadata: dict[str, Any] | None = None,
        cause: BaseException | None = None,
    ) -> None:
        super().__init__(message)
        if cause is not None:
            self.__cause__ = cause
        self.code = code
        self.context = context or ExceptionContext()
        self.metadata: dict[str, Any] = dict(metadata) if metadata else {}

    @property
    def request_id(self) -> str | None:
        return self.context.request_id

    @property
    def correlation_id(self) -> str | None:
        return self.context.correlation_id

    @property
    def trace_id(self) -> str | None:
        return self.context.trace_id

    @property
    def actor_id(self) -> str | None:
        return self.context.actor_id

    @property
    def tenant_id(self) -> str | None:
        return self.context.tenant_id


def with_metadata(options: dict[str, Any] | None, metadata: dict[str, Any]) -> dict[str, Any]:
    result = dict(options) if options else {}
    result.update(metadata)
    return result
