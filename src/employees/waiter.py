import asyncio
import uuid

# TODO: move those to init
from src.infrastructure.post_its import post_its
from src.employees.cook import cook
from src.schemas import MENU, OrderRequest


class Waiter:
    async def produce_order(self, dish_name: str):
        dish_id = MENU[dish_name]
        order = OrderRequest(id=str(uuid.uuid4()), dish_id=dish_id)
        post_its.append(order)

        cook.take_order(order)
        await asyncio.sleep(2)

        result = post_its.get(order.id)
        # TODO: manage None
        print(f"{dish_name} - {result['status']}")


waiter = Waiter()
