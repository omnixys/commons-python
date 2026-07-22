from __future__ import annotations

import re
import unicodedata


def create_tmp_username(last_name: str, first_name: str) -> str:
    raw = f"{first_name}.{last_name}".lower()
    normalized = unicodedata.normalize("NFKD", raw)
    collapsed = re.sub(r"\s+", "", normalized)
    return re.sub(r"[^\w.]", "", collapsed)
