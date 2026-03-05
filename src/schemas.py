from typing import Optional

from pydantic import BaseModel


class OrderRequest(BaseModel):
    id: str
    dish_id: int


class OrderResult(BaseModel):
    dish_id: int
    status: str
    extra: Optional[str] = None


MENU = {"Veggies": 1, "Meat": 2, "Mushrooms": 3, "Fish": 4}
