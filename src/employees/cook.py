import asyncio
import dramatiq

from src.infrastructure.post_its import post_its
from src.schemas import OrderRequest, OrderResult, OrderStatus
from src.kitchen.stove import stove


# TODO: cannot be a class method - think how to imrove
# TODO: multiple actors (cook, bartender?)
@dramatiq.actor(max_retries=3)
def cook(info: dict):
    order = OrderRequest(**info)

    async def run():
        await stove.fry(order.dish_id)
        # TODO: order result created by cook and written to storage (counter)
        # waiter reads from storage if status is ready
        post_its.update(order.id, OrderStatus.ready)

    try:
        asyncio.run(run())
    except Exception as e:
        post_its.update(order.id, OrderStatus.failed)
