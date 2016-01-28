import os

import redis

from rq import Connection, Queue


def function(*args):
    pass


def main():
    redis_url = os.getenv("REDIS_URL", "redis://127.0.0.1:6379")
    redis_conn = redis.from_url(redis_url)

    q = Queue(connection=redis_conn)
    to = ['clqRS9XO4gA:APA91bFzsMSwcCB0cMGC9LTZzRQqRNXZhffV8QaxlKVe0W14MZfQFdTiREuCNIjL3h35d0v-dsg4hSXpSI3vzojHWp4V7WnbsDAMM1pq6CvODxtRpxILb7VrKuS6JTtW5e9HxvO7kwnF',]

    with open('data.txt') as terms_file:
        terms = terms_file.read()
        for term in terms.splitlines():
            q.enqueue(function, term, to)


if __name__ == '__main__':
    with Connection():
        main()
