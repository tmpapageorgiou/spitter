from rq import Worker, Queue, Connection 

from spitter import logger
from spitter.connection import redis_conn


with Connection(redis_conn):
    worker = Worker(map(Queue, ["spitter_messages"]))
    
    logger.info("starting worker...")
    worker.work()

