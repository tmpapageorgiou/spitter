import os
import time

from rq import Connection, Queue

from spitter.connection import redis_conn


def main():
    queue = Queue("spitter_messages")
    token = ['dqeBP8JknVA:APA91bFOjIN4FG0Agabt0Fxj_SmNPpktbzZWRJXBpu9LesuOBSuaKLEO45Ln843iTM1CrfgXRqwVE4bGdcA2ozl32NRMygCvDBL7fCW2I7aD_MXm7UXIOlnLeNeiFIiiXWSUS6u9d4x2'] * 10

    for _ in range(5):
        body = "Message: %f" % time.time()
        queue.enqueue("spitter.gcm.send_notification", body, token)


with Connection(redis_conn):
    main()
