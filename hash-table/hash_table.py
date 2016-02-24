# Hash table implementation

import sys
sys.path.insert(0, '../singly-linked-list')
from singly_linked_list import LinkedList

# load factor = items / buckets

class HashTable:
    """
    An implementation for the hash table data structure
    """

    def __init__(self, bucket_count):
        self.bucket_count = bucket_count
        self.buckets = [LinkedList() for i in range(0, bucket_count)]
        self.item_count = 0

    def __getitem__(self, key):
        return self.get_value_for_key(key)

    def __setitem__(self, key, value):
        self.set_value_for_key(key, value)

    def __delitem__(self, key):
        self.remove_key(key)

    def __contains__(self, key):
        return self.contains(key)

    def set_value_for_key(self, key, value):
        def set_item(current_node):
            current_node.item = (key, value)

        if self._iterate_until_key_found(key, set_item) is None:
            bucket_index = self._get_bucket_index_for_key(key)
            linked_list = self.buckets[bucket_index]
            linked_list.insert_at_tail((key, value))

        self.item_count += 1

    def get_value_for_key(self, key):
        def return_value(current_node):
            return current_node.item[1]

        return self._iterate_until_key_found(key, return_value)

    def remove_key(self, key):
        bucket_index = self._get_bucket_index_for_key(key)
        linked_list = self.buckets[bucket_index]
        previous = None
        current_node = linked_list.head
        while current_node is not None:
            if current_node.item[0] == key:
                deleted_tuple = current_node.item
                if previous is None:
                    linked_list.delete_head()
                else:
                    previous.next = current_node.next
                self.item_count -= 1
                return deleted_tuple
            previous = current_node
            current_node = current_node.next
        return None

    def contains(self, key):
        def return_true_if_key_found(current_node):
            if current_node:
                return True

        result = self._iterate_until_key_found(key, return_true_if_key_found)
        if result is not None:
            return result
        return False

    # helper methods

    def _iterate_until_key_found(self, key, function):
        bucket_index = self._get_bucket_index_for_key(key)
        linked_list = self.buckets[bucket_index]
        current_node = linked_list.head
        while current_node is not None:
            if current_node.item[0] == key:
                return function(current_node)
            current_node = current_node.next
        return None

    def _get_bucket_index_for_key(self, key):
        hashed_key = hash(key)
        return hashed_key % self.bucket_count
