from dramatiq.brokers.rabbitmq import RabbitmqBroker
from pika import PlainCredentials


# TODO: rethink the analogy
# this seems to be the expediter
# seems that expediter = RabbitmqBroker AND dramatiq (?)
# while post it board = MongoDB, and RabbitMQ is the queue (hosted on the post-it board)
# in case of a digital tool, RabbitMQ is the queue itself still, but MongoDB is digital entries
# TODO: Broker VS dramatiq - which ones does what. Broker = communication with RabbitMQ; and dramatiq?
postit_board = RabbitmqBroker(
    # confirm_delivery=True,
    host="127.0.0.1",
    port=5672,
    virtual_host="/",
    credentials=PlainCredentials(username="restaurant", password="restaurant"),
)
