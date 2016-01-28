import os
import time

from rq import Connection
from rq import Queue

from spitter.connection import redis_conn

REPETITION = 10

def main():

    queue = Queue("spitter_messages")
    token = ['clqRS9XO4gA:APA91bFzsMSwcCB0cMGC9LTZzRQqRNXZhffV8QaxlKVe0W14MZfQFdTiREuCNIjL3h35d0v-dsg4hSXpSI3vzojHWp4V7WnbsDAMM1pq6CvODxtRpxILb7VrKuS6JTtW5e9HxvO7kwnF',]

    for _ in range(REPETITION):
        body = "Message: %f" % time.time()
        queue.enqueue("spitter.gcm.send_notification", body, token)


if __name__ == '__main__':
    with Connection(redis_conn):
        main()
