import enum
from typing import Optional

from pydantic import BaseModel


class OrderStatus(enum.StrEnum):
    ready = "ready"
    preparing = "preparing"
    failed = "failed"


class OrderRequest(BaseModel):
    id: str
    dish_id: int
    status: OrderStatus


class OrderResult(BaseModel):
    dish_name: str
    extra: Optional[str] = None


MENU: dict[str, int] = {"Veggies": 1, "Meat": 2, "Mushrooms": 3, "Fish": 4}
