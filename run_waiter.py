import asyncio
import random

from src.infrastructure.postit_board import configure_postit_board
from src.schemas import MENU

configure_postit_board()

from src.employees.waiter import produce_order

if __name__ == "__main__":
    while True:
        dish_name = random.choice(list(MENU.keys()))
        asyncio.run(produce_order(dish_name))
