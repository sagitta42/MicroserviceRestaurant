import asyncio
import random

from src.schemas import MENU, OrderRequest
from src.employees.cook import take_order


async def produce_order(dish_name: str):
    dish_id = MENU[dish_name]
    order = OrderRequest(dish_id=dish_id)

    # FIXME: object of type OrderRequest is not JSON serializable
    # take_order.send(order)
    take_order.send(order.dish_id)
    await asyncio.sleep(2)
