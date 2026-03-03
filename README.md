# Microservices Restaurant

Restaurant analogy of microservices

## Setup

1. Set up docker   
   
   ```bash
   docker compose -f docker/docker-compose.yml up -d
   ```

2. Run barker
   
   ```bash
   dramatiq run_barker
   ```

From [Wikipedia](https://en.wikipedia.org/wiki/Kitchen_brigade): Barker - takes orders from the dining room and distributes them to the various stations

3. Run waiter
   
   ```bash
   python run_waiter.py
   ```

## Restaurant analogy

Processes = employees

**Broker (RabbitmqBroker)**

- Connects to `RabbitMQ` - acts as a "mail system"

- Must be configured in each process that sends or receives 
  tasks

**--> Post-it note board with orders**

*(Note: RabbitMQ itself is the post-it note board, broker is putting/taking notes from it)
(A digital order system could be a better analogy: broker = interface to type/read orders from, RabbitMQ = order queue itself)*

**Actor / Consumer (`@dramatiq.actor`)**

Defines what to do when a message arrives

**--> Cook**

**Worker (`dramatiq`)**

- Pulls messages from `RabbitMQ` and executes actors

- Separate docker process

**--> Barker**

**Producer (`.send()`)**

- Pushes a task/message to `RabbitMQ`

- Any process that knows the actor and broker

**--> Waiter**
