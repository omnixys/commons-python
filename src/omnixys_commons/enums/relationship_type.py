from enum import StrEnum


class RelationshipType(StrEnum):
    FAMILY = "FAMILY"
    FRIEND = "FRIEND"
    PARTNER = "PARTNER"
    COLLEAGUE = "COLLEAGUE"
    OTHER = "OTHER"
    BUSINESS_PARTNER = "BUSINESS_PARTNER"
    RELATIVE = "RELATIVE"
    PARENT = "PARENT"
    SIBLING = "SIBLING"
    CHILD = "CHILD"
    COUSIN = "COUSIN"
