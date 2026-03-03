import asyncio
import dramatiq

from src.schemas import OrderRequest
from src.employees.kitchen import Kitchen

kitchen = Kitchen()

@dramatiq.actor(max_retries=3)
def take_order(dish_id: int):
    async def run():
        await kitchen.grill(dish_id)

    asyncio.run(run())