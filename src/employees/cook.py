import asyncio
import dramatiq

from src.infrastructure.post_its import post_its
from src.schemas import OrderRequest, OrderResult
from src.kitchen.stove import stove


# TODO: how can this be a class method
# TODO: rethink concept - seems that this is the expediter, not cook
# and instead of stove/kitchen THAT's the cook, the cook is the resource (human resource)
# also this should/can be running in a separate docker (consumer) (?)
@dramatiq.actor(max_retries=3)
def process_order(info: dict):
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


class Cook:
    def take_order(self, order: OrderRequest):
        process_order.send(order.model_dump())


cook = Cook()
