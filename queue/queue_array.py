# Queue array implementation

class Queue:
    """
    An implementation for the Queue data structure
    using an array.
    """

    def __init__(self, item=None):
        self.array = []
        if item is not None:
            self.array.append(item)

    def enqueue(self, item):
        """Inserts an element in the back"""
        self.array.append(item)

    def dequeue(self):
        """Removes and returns a node from the front"""
        try:
            return self.array.pop(0)
        except IndexError:
            return None

    def peek(self):
        """Gets and returns the element from the front"""
        try:
            return self.array[0]
        except IndexError:
            return None

    def clear(self):
        """Clears the whole queue"""
        self.array.clear()

    def get_size(self):
        """Returns the size of the queue"""
        return len(self.array)
