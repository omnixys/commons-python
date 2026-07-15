from __future__ import annotations

from typing import Any

from pydantic import BaseModel


class ContractSchemaNotFoundError(Exception):
    code: str = "CONTRACT_SCHEMA_NOT_FOUND"

    def __init__(self, contract: str, version: str) -> None:
        self.contract = contract
        self.version = version
        super().__init__(f"Schema not found for contract '{contract}' version '{version}'")


class ContractSchemaRegistry:
    def __init__(self) -> None:
        self._schemas: dict[str, type[BaseModel]] = {}

    def _key(self, contract: str, version: str) -> str:
        return f"{contract}@{version}"

    def register(self, contract: str, version: str, schema: type[BaseModel]) -> None:
        key = self._key(contract, version)
        self._schemas[key] = schema

    def parse(self, contract: str, version: str, value: dict[str, Any]) -> BaseModel:
        key = self._key(contract, version)
        schema = self._schemas.get(key)
        if schema is None:
            raise ContractSchemaNotFoundError(contract, version)
        return schema.model_validate(value)

    def has(self, contract: str, version: str) -> bool:
        return self._key(contract, version) in self._schemas

    def diagnostics(self) -> dict[str, list[str]]:
        return {"schemas": sorted(self._schemas.keys())}
