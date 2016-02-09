# Queue implementation

import sys
sys.path.insert(0, '../singly-linked-list')
from singly_linked_list import LinkedList

class Queue:
    """An implementation for the Queue data structure"""

    def __init__(self, item=None):
        self.linked_list = LinkedList(item)

    def push(self, item):
        self.linked_list.insert_at_tail(item)

    def dequeue(self):
        return self.linked_list.delete_head()

    def peek(self):
        return self.linked_list.head.item

    def clear(self):
        self.linked_list.clear()

    def get_size(self):
        return self.linked_list.size
