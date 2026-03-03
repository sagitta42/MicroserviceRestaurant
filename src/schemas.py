from pydantic import BaseModel


class OrderRequest(BaseModel):
    dish_id: int


class OrderResponse(BaseModel):
    dish_id: int
    ready: bool


MENU = {"Veggies": 1, "Meat": 2, "Mushrooms": 3, "Fish": 4}
