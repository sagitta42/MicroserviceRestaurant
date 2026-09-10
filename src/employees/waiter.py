import asyncio
from random import random
import uuid

# TODO: move those to init
from src.employees.cook import cook
from src.infrastructure.post_its import post_its
from src.logger import logg
from src.schemas import MENU, OrderRequest, OrderResult, OrderStatus


# FIXME: create another waiter method to get order consulting post-its - this is not async
# TODO: waiter is actually router; just send() itself is the producer action
# create api layer with waiter route, call send() in route submit order endpoint
# create another waiter endpoint to get order consulting post-its
class Waiter:
    def __init__(self):
        self._active_orders: list[str] = []
        self._inverse_menu: dict[int, str] = {value: key for key, value in MENU.items()}

    async def produce_order(self, dish_name: str):
        logg.info(f"[waiter] {dish_name}? Great choice!", header=True)
        dish_id = MENU[dish_name]
        order_id = str(uuid.uuid4()).split("-")[1]
        order = OrderRequest(id=order_id, dish_id=dish_id, status=OrderStatus.preparing)

        # TODO: create different schema for order status for MongoDB vs order pushed into queue for actor
        # TODO: where should keep customer ID
        post_its.append(order)

        self._active_orders.append(order_id)

        logg.info(f"[waiter] (order {order_id} coming through!)")
        cook.send(order.model_dump())

    async def get_orders(self) -> OrderResult | None:
        # TODO: if earliest order is not ready, keep checking others that might be ready
        cook_is_tired = random() > 0.7
        if cook_is_tired:
            logg.info(f"[waiter] taking a short break...")
            await asyncio.sleep(2)

        if len(self._active_orders) == 0:
            return None
        earliest_order_id = self._active_orders[0]
        ret = self._get_order(earliest_order_id)
        # TODO: action if order is ready; happen outside with customer
        if ret is not None:
            logg.info(
                f"[waiter] Here you go - {ret.dish_name} ({earliest_order_id})",
                header=True,
            )
        return ret

    def _get_order(self, order_id: str) -> OrderResult | None:
        order = post_its.get(order_id)
        # TODO: manage None
        assert order is not None
        dish_name = self._inverse_menu[order.dish_id]
        if order.status == OrderStatus.ready:
            self._active_orders.remove(order_id)
            # TODO: order result created by cook and written to storage (counter)
            # waiter reads from storage if status is ready
            ret = OrderResult(dish_name=dish_name)
            return ret
        else:
            logg.info(f"[waiter] (order {order_id} is  {order.status}...)")
        return None


waiter = Waiter()
