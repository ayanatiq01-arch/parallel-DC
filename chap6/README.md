# Chapter 6: Distributed Task Queue with Celery

## Overview
This chapter demonstrates distributed task processing using Celery, a powerful asynchronous task queue/job queue framework for Python. Celery enables efficient handling of background tasks, scheduled jobs, and distributed computing across multiple workers.

## Features
- Asynchronous task execution
- Distributed message passing
- Real-time operation support
- Task scheduling capabilities
- Multi-worker support

## Prerequisites
1. **Python 3.x**
2. **Celery**: Install using pip
   ```bash
   pip install celery
   ```
3. **RabbitMQ Message Broker**: Download and install from [RabbitMQ official website](https://www.rabbitmq.com/download.html)

## Installation

### Install Celery
```bash
pip install celery
```

### Install RabbitMQ
- **Windows**: Download installer from RabbitMQ website
- **Linux**: `sudo apt-get install rabbitmq-server`
- **macOS**: `brew install rabbitmq`

## Running the Application

### Step 1: Start RabbitMQ Server
```bash
rabbitmq-server
```

### Step 2: Start Celery Worker
Open a terminal in the `chap6` directory and run:
```bash
celery -A tasks worker --loglevel=info
```

### Step 3: Execute Tasks
Open Python shell or create a script:
```python
from tasks import add

result = add.delay(10, 20)
print(f"Task ID: {result.id}")
print(f"Result: {result.get(timeout=10)}")
```

## Files
- `tasks.py`: Main Celery application with task definitions

## Key Concepts

### Celery Application
The Celery instance is the entry point for everything you want to do in Celery, including creating tasks and managing workers.

### Task Decorator
The `@app.task` decorator converts a regular function into a Celery task that can be executed asynchronously.

### Message Broker
RabbitMQ acts as the message broker, facilitating communication between the Celery client and workers.

### Task Execution
- `add.delay(x, y)`: Asynchronous execution (non-blocking)
- `add.apply_async((x, y))`: Advanced asynchronous execution with options
- `add(x, y)`: Synchronous execution (blocking)

## Use Cases
- Background email sending
- Data processing pipelines
- Scheduled report generation
- Image/video processing
- Web scraping tasks
- Periodic maintenance tasks

## Further Reading
- [Celery Official Documentation](https://docs.celeryproject.org/)
- [RabbitMQ Tutorials](https://www.rabbitmq.com/getstarted.html)
