# Microservices Restaurant

A demonstration of an analogy that I invented to explain and visualize microservice software architecture / distributed systems in an intuitive way:

In this model, a waiter is the Producer while a cook in the kitchen is the Actor, and they communicate via an expediter (dramatiq) which keeps track of client orders on a post-it board (MongoDB) putting them in a queue (RabbitMQ)



| Term                      | Details                                                                                                                                                                                                  | Analogy          |                                                                                                                                                           |
| ------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Database [`MongoDB`]      |                                                                                                                                                                                                          | Post-it notes    | Source of truth on order details & status                                                                                                                 |
| Queue [`RabbitMQ`]        |                                                                                                                                                                                                          | Order system     | A system of handling customer orders, for example placing post-its on a board in received order                                                           |
| Broker [`RabbitmqBroker`] | Connects to `RabbitMQ` and stores messages received from producer in it. Provides messages to consumer threads.                                                                                          | Post-it board    | Stores post-its appended by waiter. "Provides" post-its to expediter.                                                                                     |
| `dramatiq`                | Background task processing framework that knows how to run tasks asynchronously. Flow between producer, broker, and worker threads. Relies on a broker to hold the messages. | Kitchen          | A system with cooks and expediter that manages the flow between the waiter, post-it board with orders, and cooks. Relies on post-it board to hold orders. |
| Actor [`@dramatiq.actor`] | Task logic. Defines what to do when a message arrives                                                                                                                                                    | Cook             | Recipe logic. Decides which tools in the kitchen need to be used for what recipe                                                                          |
| Producer [`.send()`]      | Pushes a task/message to `RabbitMQ` via `RabbitmqBroker`                                                                                                                                                 | Waiter           | Takes order post-its and puts them on the order board                                                                                                     |
| Worker (`dramatiq`)       | Pulls messages from `RabbitMQ` and executes actors. Separate docker process                                                                                                                              | Expediter (expo) | Pulls post-its from post-it board and distributes them to cooks. Separate person. Liason between dining room and kitchen.                                 |
| Consumer (`dramatiq`)     | Thread inside worker fetching messages from broker                                                                                                                                                       | Expediter (expo) | Expediter's brain, eyes, and hands fetching orders from the post-it board                                                                                 |
|                           | insert to MongoDB collection before `send()`                                                                                                                                                             |                  | Waiter writes out a post-it with order ID, dish ID etc. This post-it will later be marked as order ready to be picked up by the waiter later.             |

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
