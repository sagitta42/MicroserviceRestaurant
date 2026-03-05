import dramatiq

from src.infrastructure.order_board import order_board

# kitchen must set up a post-it board with orders
dramatiq.set_broker(order_board)

# kitchen has cooks
import src.employees.cook
