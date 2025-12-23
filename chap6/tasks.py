"""
Celery Distributed Task Queue Implementation

This module demonstrates the use of Celery for distributed task processing.
Celery is an asynchronous task queue/job queue based on distributed message passing.
It is focused on real-time operation but supports scheduling as well.

The execution units, called tasks, are executed concurrently on one or more worker nodes
using multiprocessing, Eventlet, or gevent. Tasks can execute asynchronously (in the background)
or synchronously (wait until ready).

Requirements:
    - Celery: pip install celery
    - RabbitMQ message broker running on localhost
    
Usage:
    1. Start RabbitMQ server
    2. Start Celery worker: celery -A tasks worker --loglevel=info
    3. Call tasks from Python shell or another script:
       from tasks import add
       result = add.delay(4, 6)
       print(result.get())
"""

from celery import Celery

app = Celery('tasks', broker='pyamqp://guest@localhost//')

@app.task
def add(x, y):
    """
    Add two numbers asynchronously using Celery task queue.
    
    Args:
        x (int/float): First number to add
        y (int/float): Second number to add
        
    Returns:
        int/float: Sum of x and y
    """
    return x + y


if __name__ == '__main__':
    result = add.delay(10, 20)
    print(f"Task ID: {result.id}")
    print(f"Task Result: {result.get(timeout=10)}")
