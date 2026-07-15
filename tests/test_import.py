"""Smoke test - verifies omnixys-commons can be imported."""

from __future__ import annotations

import importlib



def test_package_importable() -> None:
    mod = importlib.import_module("omnixys_commons")
    assert hasattr(mod, "__version__")
    assert mod.__version__ == "1.0.0"


def test_public_api() -> None:
    from omnixys_commons import dtos, enums, errors, models, schemas, utils

    assert dtos is not None
    assert enums is not None
    assert errors is not None
    assert models is not None
    assert schemas is not None
    assert utils is not None
