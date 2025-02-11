import queue as q
import threading as th


class MessagePipe():
    def __init__(self, consumer, producer):
        self.message_queue = q.Queue()

    def send(self, message_id, **kwargs):
        self.message_queue.put((message_id, kwargs))

    def consume(self):
        return self.message_queue.get()