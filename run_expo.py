import dramatiq

from src.infrastructure.order_board import postit_board

# expediter must know where the post-it board with orders is
dramatiq.set_broker(postit_board)

import src.employees.cook
