# Linked list implementation

class LinkedList:
    """An implementation for a singly linked list"""

    class Node:
        """A simple node for a single linked list"""

        def __init__(self, item):
            self.item = item
            self.next = None

    def __init__(self, item=None):
        self.head = None
        self.tail = None
        self.size = 0
        if item:
            self.head = self.Node(item)
            self.tail = self.head
            self.size = 1

    # insert operations

    def insert_at_head(self, item):
        """Inserts an item at the head."""
        new_node = self.Node(item)
        new_node.next = self.head
        if self.head == self.tail:
            self.tail = self.head
        self.head = new_node
        self.size += 1

    def insert_at_tail(self, item):
        """Inserts an item at the tail."""
        new_node = self.Node(item)
        if self.head is None:
            self.head = new_node
        if self.tail is not None:
            self.tail.next = new_node
        self.tail = new_node
        self.size += 1

    # get operations

    def get_head_item(self):
        """
        Gets and returns the head item.
        Returns None if head does not exist.
        """
        if self.head is not None:
            return self.head.item
        return None

    def get_tail_item(self):
        """
        Gets and returns the tail item.
        Returns None if tail does not exist.
        """
        if self.tail is not None:
            return self.tail
        return None

    def get_item_at_index(self, index):
        """
        Gets and returns the item at the given index.
        Raises an IndexError if index is out of range.
        """
        if type(index) is not int:
            raise ValueError("Invalid index")
        if index >= self.size:
            raise IndexError("Index out of range: {}".format(index))
        current_node = self.head
        i = 0
        while current_node is not None:
            if i == index:
                return current_node.item
            i += 1
            current_node = current_node.next

    # search operations

    def search_for_item(self, item):
        """
        Searches for nodes containing the item.
        Returns the first index in which the item
        is found.
        """
        current_node = self.head
        index = 0
        while current_node is not None:
            if current_node.item == item:
                return (index, item)
            current_node = current_node.next
            index += 1
        return None

    def search_for_all_item(self, item):
        """
        Searches through the whole linked list for the item.
        Returns an array of tuples containing the indexes and items.
        """
        items_array = []
        current_node = self.head
        index = 0
        while current_node is not None:
            if current_node.item == item:
                items_array.append((index, item))
            current_node = current_node.next
            index += 1
        return items_array

    # remote operations

    def delete_head(self):
        """
        Removes the item at head.
        Returns the deleted item.
        Raises ValueError if there is no Head.
        """
        if self.head is not None:
            old_head = self.head
            self.head = old_head.next
            old_head.next = None
            if self.head is None:
                self.tail = None
            self.size -= 1
            return old_head.item
        else:
            return None

    def delete_tail(self):
        """
        Removes the item at the tail.
        Returns the deleted item.
        Raises ValueError if there is no tail.
        """
        if self.tail is not None:
            current_node = self.head
            while current_node is not None:
                if current_node.next.next is None:
                    # current_node.next.next is the tail
                    deleted_item = current_node.next.item
                    current_node.next = None
                    self.tail = current_node.next
                    self.size -= 1
                    return deleted_item
                current_node = current_node.next
        else:
            raise ValueError("Tail does not exist")

    def delete_item_at_index(self, index):
        """
        Deletes an item at the given index.
        Returns the deleted item.
        Raises IndexError if index is out of range.
        """
        if type(index) is not int:
            raise ValueError("Invalid index")
        if index >= self.size:
            raise IndexError("Index out of range: {}".format(index))
        current_node = self.head
        previous = None
        i = 0
        while current_node is not None:
            if i == index:
                previous.next = current_node.next
                current_node.next = None
                self.size -= 1
                return current_node.item
            previous = current_node
            current_node = current_node.next
            i+= 1

    def clear(self):
        """
        Removes all nodes in the linked list.
        """
        while self.delete_head() is not None:
            self.delete_head()
