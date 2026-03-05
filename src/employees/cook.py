import asyncio
import dramatiq

from src.infrastructure.post_its import post_its
from src.schemas import OrderRequest, OrderResult
from src.kitchen.stove import stove


# TODO: cannot be a class method - think how to imrove
# TODO: multiple actors (cook, bartender?)
@dramatiq.actor(max_retries=3)
def cook(info: dict):
    order = OrderRequest(**info)

    async def run():
        ready = await stove.fry(order.dish_id)
        result = OrderResult(dish_id=order.dish_id, status="ready")
        post_its.update(order.id, result)

    try:
        asyncio.run(run())
    except Exception as e:
        result = OrderResult(dish_id=order.dish_id, status="failed", extra=str(e))
        post_its.update(order.id, result)
