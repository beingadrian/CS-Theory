import unittest
from singly_linked_list import LinkedList

class TestSinglyLinkedList(unittest.TestCase):

    def setUp(self):
        self.linked_list = LinkedList()

    def test_empty_init(self):
        self.assertEqual(self.linked_list.size, 0)
        self.assertIsNone(self.linked_list.head)
        self.assertIsNone(self.linked_list.tail)

    def test_init_with_item(self):
        linked_list = LinkedList("Bob")
        self.assertEqual(linked_list.size, 1)
        self.assertIsNotNone(linked_list.head)
        self.assertIsNotNone(linked_list.tail)
        self.assertEqual(linked_list.head, linked_list.tail)

    def test_insert_at_head(self):
        initial_size = self.linked_list.size
        self.linked_list.insert_at_head("Tom")
        self.assertIsNotNone(self.linked_list.head)
        self.assertEqual(self.linked_list.size, initial_size + 1)
        self.assertEqual(self.linked_list.head.item, "Tom")

    def test_insert_at_tail(self):
        initial_size = self.linked_list.size
        self.linked_list.insert_at_tail("Bob is your uncle")
        self.assertEqual(self.linked_list.tail.item, "Bob is your uncle")
        self.assertIsNotNone(self.linked_list.tail)
        self.assertEqual(self.linked_list.size, initial_size + 1)
        empty_linked_list = LinkedList()
        empty_initial_size = empty_linked_list.size
        empty_linked_list.insert_at_tail("Bob")
        self.assertIsNotNone(empty_linked_list.head)
        self.assertIsNotNone(empty_linked_list.tail)
        self.assertEqual(empty_linked_list.size, empty_initial_size + 1)

    def test_get_head_item_with_no_head(self):
        item = self.linked_list.get_head_item()
        self.assertIsNone(item)

    def test_get_head_with_item(self):
        linked_list = LinkedList("Bob")
        item = linked_list.get_head_item()
        self.assertIsNotNone(item)
        self.assertEqual(item, "Bob")

    def test_get_tail_item(self):
        empty_linked_list = LinkedList()
        empty_item = empty_linked_list.get_tail_item()
        self.assertIsNone(empty_item)
        linked_list = LinkedList("Bob")
        item = linked_list.get_tail_item()
        self.assertIsNotNone(item)

    def test_get_item_at_index(self):
        self.linked_list.insert_at_tail("Adrian")
        self.linked_list.insert_at_tail("Bob")
        self.linked_list.insert_at_tail("Chris")
        item = self.linked_list.get_item_at_index(2)
        self.assertEqual(item, "Chris")
        with self.assertRaises(IndexError):
            new_item = self.linked_list.get_item_at_index(5)

    def test_search_for_item(self):
        linked_list = LinkedList("Bob")
        linked_list.insert_at_tail("Kim")
        linked_list.insert_at_tail("Jim")
        linked_list.insert_at_tail("Max")
        result = linked_list.search_for_item("Max")
        self.assertEqual(result, (3, "Max"))
        empty_result = linked_list.search_for_item("Adrian")
        self.assertIsNone(empty_result)

    def test_search_for_all_item(self):
        linked_list = LinkedList("Bob")
        linked_list.insert_at_tail("Kim")
        linked_list.insert_at_tail("Bob")
        linked_list.insert_at_tail("Bob")
        result = linked_list.search_for_all_item("Bob")
        self.assertEqual(len(result), 3)

    def test_delete_head(self):
        self.linked_list.insert_at_head("Bob")
        initial_size = self.linked_list.size
        deleted_item = self.linked_list.delete_head()
        self.assertEqual(self.linked_list.size, initial_size - 1)
        self.assertEqual(deleted_item, "Bob")
        self.assertIsNone(self.linked_list.head)
        self.assertIsNone(self.linked_list.tail)
        new_linked_list = LinkedList("Adrian")
        new_linked_list.insert_at_head("Bob")
        new_deleted_item = new_linked_list.delete_head()
        self.assertEqual(new_deleted_item, "Bob")
        self.assertEqual(new_linked_list.tail.item, "Adrian")
        self.assertEqual(new_linked_list.head.item, "Adrian")

    def test_delete_tail(self):
        self.linked_list.insert_at_tail("Bob")
        self.linked_list.insert_at_tail("Jim")
        self.linked_list.insert_at_tail("Ryan")
        self.linked_list.insert_at_tail("Tim")
        initial_size = self.linked_list.size
        deleted_item = self.linked_list.delete_tail()
        self.assertEqual(self.linked_list.size, initial_size - 1)
        self.assertEqual(deleted_item, "Tim")

    def test_delete_at_index(self):
        self.linked_list.insert_at_tail("Adam")
        self.linked_list.insert_at_tail("Bob")
        self.linked_list.insert_at_tail("Chris")
        self.linked_list.insert_at_tail("Dylan")
        initial_size = self.linked_list.size
        deleted_item = self.linked_list.delete_item_at_index(3)
        self.assertEqual(self.linked_list.size, initial_size - 1)
        self.assertEqual(deleted_item, "Dylan")
        with self.assertRaises(IndexError):
            self.linked_list.delete_item_at_index(5)
        with self.assertRaises(ValueError):
            self.linked_list.delete_item_at_index("Bla")

    def test_clear(self):
        self.linked_list.insert_at_tail("Adam")
        self.linked_list.insert_at_tail("Bob")
        self.linked_list.insert_at_tail("Chris")
        self.linked_list.insert_at_tail("Dylan")
        self.linked_list.insert_at_tail("Erin")
        self.linked_list.clear()
        self.assertEqual(self.linked_list.size, 0)

if __name__ == '__main__':
    unittest.main()
