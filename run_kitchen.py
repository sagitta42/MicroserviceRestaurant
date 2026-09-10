import dramatiq

from src.infrastructure.expediter import expediter

# kitchen order system is managed by expediter
dramatiq.set_broker(expediter)

# kitchen has cooks
import src.employees.cook
