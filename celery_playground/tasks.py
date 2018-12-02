from __future__ import absolute_import, unicode_literals
from .celery import app
import random


@app.task(bind=True)
def add(self, x, y):
    num = random.randint(1, 10)
    try:
        if num < 7:
            raise Exception()
        else:
            return x + y
    except Exception as e:
        self.retry(countdown=5, exc=e, max_retries=3)


@app.task
def mul(x, y):
    return x * y


@app.task
def xsum(numbers):
    return sum(numbers)
