import asyncio
from typing import Any
import uuid

# TODO: move those to init
from src.employees.cook import cook
from src.infrastructure.post_its import post_its
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
        dish_id = MENU[dish_name]
        order_id = str(uuid.uuid4())
        order = OrderRequest(id=order_id, dish_id=dish_id, status=OrderStatus.preparing)

        # TODO: create different schema for order status for MongoDB vs order pushed into queue for actor
        # TODO: where should keep customer ID
        post_its.append(order)

        self._active_orders.append(order_id)

        cook.send(order.model_dump())

    async def get_orders(self) -> OrderResult | None:
        if len(self._active_orders) == 0:
            return None
        earliest_order = self._active_orders[0]
        ret = self._get_order(earliest_order)
        # TODO: action if order is ready
        if ret is not None:
            print(f"Here you go - {ret.dish_name}")
        return ret

    def _get_order(self, order_id: str) -> OrderResult | None:
        order = post_its.get(order_id)
        # TODO: manage None
        assert order is not None
        dish_name = self._inverse_menu[order.dish_id]
        print(f"Order {order_id} - {dish_name} - {order.status}")
        if order.status == OrderStatus.ready:
            self._active_orders.remove(order_id)
            # TODO: order result created by cook and written to storage (counter)
            # waiter reads from storage if status is ready
            ret = OrderResult(dish_name=dish_name)
            return ret
        return None


waiter = Waiter()
