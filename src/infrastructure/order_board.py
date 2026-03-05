from dramatiq.brokers.rabbitmq import RabbitmqBroker
from pika import PlainCredentials


order_board = RabbitmqBroker(
    # confirm_delivery=True,
    host="127.0.0.1",
    port=5672,
    virtual_host="/",
    credentials=PlainCredentials(username="restaurant", password="restaurant"),
)
