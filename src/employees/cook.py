import asyncio
import dramatiq
from random import random

from src.infrastructure.post_its import post_its
from src.schemas import OrderRequest, OrderStatus
from src.kitchen.stove import stove


# TODO: cannot be a class method - think how to imrove
# TODO: multiple actors (cook, bartender?)
@dramatiq.actor(max_retries=3)
def cook(info: dict):
    order = OrderRequest(**info)

    async def run():
        print(f"[cook] {order.id} coming right up!")
        await stove.fry(order.dish_id)
        # TODO: order result created by cook and written to storage (counter)
        # waiter reads from storage if status is ready
        post_its.update(order.id, OrderStatus.ready)
        print(f"[cook] {order.id} done cooking!")
        cook_is_tired = random() > 0.7
        if cook_is_tired:
            print(f"[cook] taking a short break...")
            await asyncio.sleep(2)

    try:
        asyncio.run(run())
    except Exception as e:
        post_its.update(order.id, OrderStatus.failed)
        print(f"[cook] {order.id} got messed up!")
