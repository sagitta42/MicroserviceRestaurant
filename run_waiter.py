import asyncio
from time import sleep
import dramatiq

from src.customers import Customers
from src.infrastructure.expediter import expediter
from src.schemas import MENU

# customer order system is managed by expediter
dramatiq.set_broker(expediter)

# waiter must arrive after the expediter is ready and order baord is good to go
from src.employees.waiter import waiter

if __name__ == "__main__":
    customers = Customers()
    while True:
        dish_name = customers.make_order()
        asyncio.run(waiter.produce_order(dish_name))
        sleep(2)
        # TODO: action if order is ready
        asyncio.run(waiter.get_orders())
