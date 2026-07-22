from __future__ import annotations

from dataclasses import dataclass, field

from commons.models.validation_error import ValidationError


@dataclass(slots=True)
class ApiResponse[T]:
    success: bool
    data: T | None = None
    message: str | None = None
    errors: list[ValidationError] = field(default_factory=list)

    @staticmethod
    def ok(data: T, message: str | None = None) -> ApiResponse[T]:
        return ApiResponse(success=True, data=data, message=message)

    @staticmethod
    def error(message: str, errors: list[ValidationError] | None = None) -> ApiResponse[None]:
        return ApiResponse(success=False, message=message, errors=errors or [])
