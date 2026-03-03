import asyncio

from src.schemas import MENU, OrderRequest
from src.employees.cook import cook


class Waiter:
    async def produce_order(self, dish_name: str):
        dish_id = MENU[dish_name]
        order = OrderRequest(dish_id=dish_id)

        cook.take_order(order)
        await asyncio.sleep(2)


waiter = Waiter()
