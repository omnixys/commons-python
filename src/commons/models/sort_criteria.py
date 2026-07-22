from __future__ import annotations

from typing import TypeVar

from pydantic import BaseModel

from commons.enums.sort_direction import SortDirection

T = TypeVar("T")


class SortCriteria(BaseModel):
    field: str
    direction: SortDirection = SortDirection.ASC


class SortCriterias[T](BaseModel):
    sort: list[SortCriteria] = []
