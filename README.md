# omnixys-commons

Omnixys shared platform contracts — transport-neutral DTOs, enums, errors, models, and schemas shared by all Omnixys services.

## Installation

```bash
pip install omnixys-commons
```

## Features

- **DTOs**: transport Data Transfer Objects for API communication (`commons.dtos`)
- **Enums**: shared enumerations across services, including the full event permission model (`commons.enums`)
- **Errors**: standardized error handling with a stable wire vocabulary — `ErrorCode` (~130 codes), `OmnixysException`, and domain exceptions (`commons.errors`)
- **Models**: Pydantic domain models for API responses, pagination, envelopes, and identity (`commons.models`)
- **Schemas**: versioned contract schemas with a `ContractSchemaRegistry` for `MAJOR.MINOR`-versioned parsing (`commons.schemas`)
- **Utils**: locale mapping, phone-number extraction, username generation, event-role permissions, and null↔undefined helpers (`commons.utils`)

## Usage

### Errors

```python
from commons.errors import ErrorCode, OmnixysException, is_error_code, with_metadata

raise OmnixysException(ErrorCode.EVENT_CLOSED, "Event is closed", metadata={"eventId": "..."})
assert is_error_code("EVENT_NOT_FOUND") is True
```

Domain exceptions carry their wire code:

```python
from commons.errors import EventNotFoundException

try:
    ...
except EventNotFoundException as exc:
    exc.code          # "EVENT_NOT_FOUND"
    exc.request_id    # from ExceptionContext
    exc.metadata
```

### Contract schema registry

```python
from pydantic import BaseModel
from commons.schemas import ContractSchemaRegistry

class UserContract(BaseModel):
    name: str

registry = ContractSchemaRegistry()
registry.register("user", "1.0", UserContract)
user = registry.parse("user", "1.0", {"name": "Ada"})
```

### Pagination

```python
from commons.models import PaginationResponse

resp = PaginationResponse(items=[1, 2, 3], total=25, page=0, size=10)
resp.total_pages   # 3
resp.has_next      # True
```

### Utilities

```python
from commons.utils import get_primary_phone_number, unique_event_permissions

primary = get_primary_phone_number(phone_numbers)   # "+49..." or None
perms = unique_event_permissions(["event.view", "event.view"])
```

## License

GPL-3.0-or-later
