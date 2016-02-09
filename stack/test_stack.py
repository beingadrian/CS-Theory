# Stack tests

import unittest
from stack import Stack

class TestStack(unittest.TestCase):

    def setUp(self):
        self.stack = Stack()

    def test_init(self):
        self.assertEqual(self.stack.get_size(), 0)
        new_stack = Stack("Bob")
        self.assertEqual(new_stack.get_size(), 1)

    def test_push(self):
        initial_size = self.stack.get_size()
        self.stack.push("Bob")
        self.assertEqual(self.stack.get_size(), initial_size + 1)

    def test_peek(self):
        self.stack.push("Adrian")
        self.stack.push("Bob")
        self.stack.push("Claire")
        self.assertEqual(self.stack.peek(), "Claire")

    def test_pop(self):
        self.stack.push("Adrian")
        self.stack.push("Bob")
        self.stack.push("Claire")
        initial_size = self.stack.get_size()
        popped_item = self.stack.pop()
        self.assertEqual(popped_item, "Claire")
        self.assertEqual(self.stack.get_size(), initial_size - 1)

    def test_clear(self):
        self.stack.push("Adrian")
        self.stack.push("Bob")
        self.stack.push("Claire")
        self.assertEqual(self.stack.get_size(), 3)
        self.stack.clear()
        self.assertEqual(self.stack.get_size(), 0)

    def test_get_size(self):
        self.stack.push("Bob")
        self.assertEqual(self.stack.linked_list.size, self.stack.get_size())


if __name__ == '__main__':
    unittest.main()
