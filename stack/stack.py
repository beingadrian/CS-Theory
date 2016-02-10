# Stack implementation

import sys
sys.path.insert(0, '../singly-linked-list')
from singly_linked_list import LinkedList

class Stack:
    """An implementation for the Stack data structure"""

    def __init__(self, item=None):
        self.linked_list = LinkedList(item)

    def push(self, item):
        """Pushes an element onto the top of the stack"""
        self.linked_list.insert_at_head(item)

    def peek(self):
        """Gets and returns an element from the top of the stack"""
        return self.linked_list.get_head_item()

    def pop(self):
        """Removes and returns the element on top of the stack"""
        return self.linked_list.delete_head()

    def clear(self):
        """Removes all the elements form the stack"""
        self.linked_list.clear()

    def get_size(self):
        """Returns the size of the stack"""
        return self.linked_list.size
