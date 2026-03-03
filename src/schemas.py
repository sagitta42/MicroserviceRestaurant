from pydantic import BaseModel


class OrderRequest(BaseModel):
    dish_id: int


class OrderResponse(BaseModel):
    dish_id: int
    ready: bool


MENU = {"Veggies": 1, "Sausage": 2, "Mushrooms": 3, "Polenta": 4}
