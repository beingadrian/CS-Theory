# Stack implementation

import sys
sys.path.insert(0, '../singly-linked-list')
from singly_linked_list import LinkedList

class Stack(object):
    """An implementation for the Stack data structure"""

    def __init__(self, item=None):
        self.linked_list = LinkedList(item)

    def push(self, item):
        self.linked_list.insert_at_head(item)

    def peek(self):
        return self.linked_list.get_head_item()

    def pop(self):
        return self.linked_list.delete_head()

    def clear(self):
        self.linked_list.clear()

    def get_size(self):
        return self.linked_list.size
