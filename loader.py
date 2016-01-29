import os
import time

from rq import Connection, Queue

from spitter.connection import redis_conn


REPETITION = 10

def main():

    queue = Queue("spitter_messages")
    token = ['dqeBP8JknVA:APA91bFOjIN4FG0Agabt0Fxj_SmNPpktbzZWRJXBpu9LesuOBSuaKLEO45Ln843iTM1CrfgXRqwVE4bGdcA2ozl32NRMygCvDBL7fCW2I7aD_MXm7UXIOlnLeNeiFIiiXWSUS6u9d4x2'] * 100
#    token = ['clqRS9XO4gA:APA91bFzsMSwcCB0cMGC9LTZzRQqRNXZhffV8QaxlKVe0W14MZfQFdTiREuCNIjL3h35d0v-dsg4hSXpSI3vzojHWp4V7WnbsDAMM1pq6CvODxtRpxILb7VrKuS6JTtW5e9HxvO7kwnF'] * 5

    for _ in range(REPETITION):
        body = "Message: %f" % time.time()
        queue.enqueue("spitter.gcm.send_notification", body, token)


if __name__ == '__main__':
    with Connection(redis_conn):
        main()
