# Queue implementation

import sys
sys.path.insert(0, '../singly-linked-list')
from singly_linked_list import LinkedList

class Queue:
    """An implementation for the Queue data structure"""

    def __init__(self, item=None):
        self.linked_list = LinkedList(item)

    def push(self, item):
        """Inserts an element in the back"""
        self.linked_list.insert_at_tail(item)

    def dequeue(self):
        """Removes a node from the front"""
        return self.linked_list.delete_head()

    def peek(self):
        """Gets and returns the element from the front"""
        return self.linked_list.head.item

    def clear(self):
        """Clears the whole queue"""
        self.linked_list.clear()

    def get_size(self):
        """Returns the size of the queue"""
        return self.linked_list.size
