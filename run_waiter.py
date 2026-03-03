import asyncio
import random

from src.customers import Customers
from src.infrastructure.postit_board import configure_postit_board
from src.schemas import MENU

configure_postit_board()

from src.employees.waiter import produce_order

if __name__ == "__main__":
    customers = Customers()
    while True:
        dish_name = customers.make_order()
        asyncio.run(produce_order(dish_name))
