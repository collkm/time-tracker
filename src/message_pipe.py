import queue as q
import threading as th
import json as json


class MessagePipe():
    """Pipe for routing messages to consumers. Each consumer must register for all receivable messages using message IDs."""
    def __init__(self):
        self.message_queues = { }
        self.queue_key = { }

    def send(self, message_id, **kwargs):
        """Sends the given message to all registered consumers."""
        if message_id in self.queue_key:
            for queue in self.queue_key[message_id]:
                queue.put((message_id, json.dumps(kwargs)))

    def consume(self, consumer_id):
        """Returns all messages queued for the consumer with the given consumer_id."""
        messages = [ ]
        for message in self.message_queues[consumer_id]:
            messages.append((message[0], json.loads(message[1])))
        return messages

    def register_consumer(self, consumer_id, message_ids):
        """
        Registers the consumer with the given consumer_id and creates an input queue for that consumer.
        Returns the method to consume messages.
        """
        if consumer_id not in self.message_queues:
            self.message_queues[consumer_id] = q.Queue()
        consumer_queue = self.message_queues[consumer_id]
        for message_id in message_ids:
            if message_id not in self.queue_key:
                self.queue_key[message_id] = [consumer_queue]
            self.queue_key[message_id].append(consumer_queue)
        return self.consume

    def register_sender(self):
        """Privides a method for senders to send messages."""
        return self.send