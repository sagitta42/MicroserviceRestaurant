# Microservices Restaurant

A demonstration of an analogy that I invented to explain and visualize asynchronous message-driven task queue architecture in an intuitive way:

In this model, a waiter is the Producer while a cook in the kitchen Service is the Actor, and they communicate via an expediter Broker which keeps track of customer order Payloads using MongoDB post-its queueing up order tickets on a RabbitMQ post-it board.

| Component                 | Details                                                      | Analogy               | Reasoning                                                    |
| ------------------------- | ------------------------------------------------------------ | --------------------- | ------------------------------------------------------------ |
| Task DB [`MongoDB`]       | Database to keep track of task status                        | Post-it notes         | Source of truth on order details & status                    |
| Queue [`RabbitMQ`]        | Task queue                                                   | Post-it board         | A system of handling customer orders, for example hanging order slips on a board in received order |
| Broker [`RabbitmqBroker`] | Connects to `RabbitMQ` and stores messages received from producer in it. Provides messages to consumer threads. | Expediter             | Takes order notes from waiter and appends them to the order board. |
| `dramatiq`                | Background task processing framework that knows how to run tasks asynchronously. Flow between producer, broker, and worker threads. Relies on a broker to hold the messages. | Order handling system | A system to manage multiple orders with multiple cooks working in parallel. Options: order slip board, digital order system, whiteboard |
| Actor [`@dramatiq.actor`] | Task logic. Defines what to do when a message arrives        | Cook, bartender       | Calls kitchen/bar service to execute order                   |
| Producer [`.send()`]      | Pushes a task/message to `RabbitMQ` via `RabbitmqBroker`     | Waiter                | Takes order post-its and puts them on the order board        |
| Worker (`dramatiq`)       | Pulls messages from `RabbitMQ` and executes actors.          | Expediter             | Pulls order notes from order board and distributes them to cooks. Liason between dining room and kitchen. |
| Consumer (`dramatiq`)     | Thread inside worker fetching messages from broker           | Expediter (expo)      | Expediter's brain, eyes, and hands fetching orders from the post-it board |
|                           | insert to MongoDB collection before `send()`                 |                       | Waiter writes out a post-it with order ID, dish ID etc. This post-it will later be marked as order ready to be picked up by the waiter later. |
| Service                   |                                                              | Kitchen, bar          | Kitchen service defines which tools in the kitchen need to be used for what recipe (pizza service, side dish service); drinks service defines how to make drinks |
| Engine                    | Core logic a.k.a. business logic                             | Kitchen tools         | Oven, stove, deep fryer etc.                                 |

From [Wikipedia](https://en.wikipedia.org/wiki/Kitchen_brigade): Expediter (Expo) - takes orders from the dining room and distributes them to the various stations

## Setup

0. Environment
   
   ```bash
   python -m venv venv
   source venv/bin/activate
   poetry install --no-root
   ```

1. Set up docker   
   
   ```bash
   docker compose -f docker/docker-compose.yml up -d
   ```

2. Run kitchen
   
   ```bash
   dramatiq run_kitchen
   ```

Note: kitchen must be run first before the waiter - otherwise waiter's orders won't have anywhere to go

TODO: docker service

3. Run waiter
   
   ```bash
   python run_waiter.py
   ```


-----
*Made using [poetiq](https://pypi.org/project/poetiq)*
