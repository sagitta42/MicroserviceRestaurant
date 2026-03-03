import asyncio
import dramatiq

from src.schemas import OrderRequest
from src.kitchen.stove import stove


@dramatiq.actor(max_retries=3)
def process_order(dish_id: int):
    async def run():
        await stove.fry(dish_id)

    asyncio.run(run())


class Cook:
    def take_order(self, order: OrderRequest):
        process_order.send(order.dish_id)


cook = Cook()
