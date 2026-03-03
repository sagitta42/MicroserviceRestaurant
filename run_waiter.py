import asyncio
import dramatiq

from src.customers import Customers
from src.infrastructure.order_board import postit_board
from src.schemas import MENU

# expediter must know where the post-it board with orders is
dramatiq.set_broker(postit_board)

# waiter must arrove after the board is set up and expo is good to go
from src.employees.waiter import waiter

if __name__ == "__main__":
    customers = Customers()
    while True:
        dish_name = customers.make_order()
        asyncio.run(waiter.produce_order(dish_name))
