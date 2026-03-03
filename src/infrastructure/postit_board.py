import dramatiq
from dramatiq.brokers.rabbitmq import RabbitmqBroker
from pika import PlainCredentials


def configure_postit_board():
    broker = RabbitmqBroker(
        # confirm_delivery=True,
        host="127.0.0.1",
        port=5672,
        virtual_host="/",
        credentials=PlainCredentials(
            username="weather",
            password="weather"
        )
    )
    dramatiq.set_broker(broker)
