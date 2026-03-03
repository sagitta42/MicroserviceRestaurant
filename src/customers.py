import random

from src.schemas import MENU


class Customers:
    def make_order(self) -> str:
        dish_name = random.choice(list(MENU.keys()))
        return dish_name
