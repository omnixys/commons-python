from __future__ import annotations

from dataclasses import dataclass, field

from omnixys_commons.enums.sort_direction import SortDirection


@dataclass(frozen=True, slots=True)
class SortCriteria:
    field_name: str
    direction: SortDirection = SortDirection.ASC

    @staticmethod
    def asc(field_name: str) -> SortCriteria:
        return SortCriteria(field_name=field_name, direction=SortDirection.ASC)

    @staticmethod
    def desc(field_name: str) -> SortCriteria:
        return SortCriteria(field_name=field_name, direction=SortDirection.DESC)


@dataclass(frozen=True, slots=True)
class PaginationRequest:
    page: int = 0
    size: int = 20
    sort: tuple[SortCriteria, ...] = ()


@dataclass(slots=True)
class PaginationResponse[T]:
    items: list[T] = field(default_factory=list)
    total: int = 0
    page: int = 0
    size: int = 20

    @property
    def total_pages(self) -> int:
        if self.size <= 0:
            return 0
        return -(-self.total // self.size)

    @property
    def has_next(self) -> bool:
        return self.page < self.total_pages - 1

    @property
    def has_previous(self) -> bool:
        return self.page > 0
