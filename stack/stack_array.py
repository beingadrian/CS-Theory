# Stack array implementation

class Stack:
    """
    An implementation for the Stack data structure
    using an array.
    """

    def __init__(self, item=None):
        self.array = []
        if item is not None:
            self.array.append(item)

    def push(self, item):
        """Pushes an element onto the top of the stack"""
        self.array.append(item)

    def peek(self):
        """Gets and returns an element from the top of the stack"""
        return self.array[len(self.array) - 1]

    def pop(self):
        """Removes and returns the element on top of the stack"""
        return self.array.pop()

    def clear(self):
        """Removes all the elements form the stack"""
        self.array.clear()

    def get_size(self):
        """Returns the size of the stack"""
        return len(self.array)
