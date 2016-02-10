# Queue array tests

import unittest
from queue_array import Queue

class TestStack(unittest.TestCase):

    def setUp(self):
        self.queue = Queue()

    def test_init(self):
        self.assertEqual(self.queue.get_size(), 0)
        new_queue = Queue("Bob")
        self.assertEqual(new_queue.get_size(), 1)

    def test_enqueue(self):
        self.queue.enqueue("Bob")
        self.assertEqual(self.queue.get_size(), 1)

    def test_dequeue(self):
        self.queue.enqueue("Bob")
        dequeued_item = self.queue.dequeue()
        self.assertEqual(dequeued_item, "Bob")
        another_dequeued_item = self.queue.dequeue()
        self.assertIsNone(another_dequeued_item)

    def test_peek(self):
        self.queue.enqueue("Bob")
        self.queue.enqueue("Bill")
        self.queue.enqueue("Boris")
        peeked_item = self.queue.peek()
        self.assertEqual(peeked_item, "Bob")

    def test_clear(self):
        for i in range(0, 100):
            self.queue.enqueue("Bob")
        self.assertEqual(self.queue.get_size(), 100)
        self.queue.clear()
        self.assertEqual(self.queue.get_size(), 0)

    def test_get_size(self):
        self.assertEqual(self.queue.get_size(), 0)


if __name__ == '__main__':
    unittest.main()
