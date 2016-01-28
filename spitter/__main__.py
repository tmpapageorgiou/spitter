from rq import Worker
from rq import Queue
from rq import Connection

from spitter import logger
from spitter.connection import redis_conn


with Connection(redis_conn):
    queue = Queue("spitter_messages")

    logger.info("starting worker...")

    Worker(queue).work()
