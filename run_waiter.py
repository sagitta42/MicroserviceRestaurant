import asyncio

from src.customers import Customers
from src.employees.expo import configure_expo
from src.schemas import MENU

configure_expo()

from src.employees.waiter import produce_order

if __name__ == "__main__":
    customers = Customers()
    while True:
        dish_name = customers.make_order()
        asyncio.run(produce_order(dish_name))
