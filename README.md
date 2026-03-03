# Restaurant

Microservices restaurant

## Setup

1. Set up docker
```bash
docker compose -f docker/docker-compose.yml up -d
```

2. Run worker

```bash
dramatiq run_worker
```

3. Run calls with producer

```bash
python -m src.workers.producer
```

## Restaurant analogy

Processes = employees

Actor / Consumer function (@dramatiq.actor)
Defines what to do when a message arrives
--> cook

Worker (dramatiq run_worker)
Pulls messages from RabbitMQ and executes actors
Separate OS process
--> barker

Producer / .send()
Pushes a task/message to RabbitMQ
Any process that knows the actor and broker
--> waiter

Broker (RabbitmqBroker)
Connects to RabbitMQ — acts as a "mail system"
Must be configured in each process that sends or receives tasks
--> Post-it note board with orders
(Note: RabbitMQ itself is the post-it note board, broker is putting/taking notes from it)
(Taking a digital order system, broker = interface to type/read orders from, RabbitMQ = order queue itself)