# Queue tests

import unittest
from queue import Queue

class TestStack(unittest.TestCase):

    def setUp(self):
        self.queue = Queue()

    def test_init(self):
        self.assertEqual(self.queue.get_size(), 0)
        new_queue = Queue("Bob")
        self.assertEqual(new_queue.get_size(), 1)

    def test_push(self):
        self.queue.push("Bob")
        self.assertEqual(self.queue.get_size(), 1)

    def test_dequeue(self):
        self.queue.push("Bob")
        dequeued_item = self.queue.dequeue()
        self.assertEqual(dequeued_item, "Bob")
        another_dequeued_item = self.queue.dequeue()
        self.assertIsNone(another_dequeued_item)

    def test_peek(self):
        self.queue.push("Bob")
        self.queue.push("Bill")
        self.queue.push("Boris")
        peeked_item = self.queue.peek()
        self.assertEqual(peeked_item, "Bob")

    def test_clear(self):
        for i in range(0, 100):
            self.queue.push("Bob")
        self.assertEqual(self.queue.get_size(), 100)
        self.queue.clear()
        self.assertEqual(self.queue.get_size(), 0)

    def test_get_size(self):
        self.assertEqual(self.queue.get_size(), self.queue.linked_list.size)


if __name__ == '__main__':
    unittest.main()
