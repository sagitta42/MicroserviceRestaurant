# Microservices Restaurant

Restaurant analogy of microservices

| Term                      | Details                                            | Analogy                          |                                                                                      |
| ------------------------- | -------------------------------------------------- | -------------------------------- | ------------------------------------------------------------------------------------ |
| Processes                 |                                                    | Employees                        |                                                                                      |
| Database [`MongoDB`]      |                                                    | Post-it notes                    | Source of truth on order details & status                                            |
| Queue [`RabbitMQ`]        |                                                    | Order system                     | A system of handling customer orders, for example placing post-its in received order |
| Broker [`RabbitmqBroker`] | Connects to `RabbitMQ`                             | Order queue                      | A way to connect and read to the queue, for example a board where to put post-its    |
| Worker (`dramatiq`)       | Pulls messages from `RabbitMQ` and executes actors | Expediter (expo)                 | Takes orders from post-it order board and distributes among cooks                    |
|                           | Separate docker process                            |                                  | Liason between dining room and kitchen                                               |
| Actor [`@dramatiq.actor`] | Defines what to do when a message arrives          | Cook | Decides which tools in the kitchen need to be used for what recipe                   |
| Producer [`.send()`]      | Pushes a task/message to `RabbitMQ`                | Waiter                           | Takes orders from customers and puts post-its on the order board                     |

## Setup

0. Environment
   
   ```bash
   python3.11 -m venv venv
   source venv/bin/activate
   poetry install --no-root
   ```

1. Set up docker   
   
   ```bash
   docker compose -f docker/docker-compose.yml up -d
   ```

2. Run expo
   
   ```bash
   dramatiq run_expo
   ```

From [Wikipedia](https://en.wikipedia.org/wiki/Kitchen_brigade): Expediter (Expo) - takes orders from the dining room and distributes them to the various stations

Note: expo must be run first before the waiter - otherwise waiter's orders won't have anywhere to go

3. Run waiter
   
   ```bash
   python run_waiter.py
   ```
