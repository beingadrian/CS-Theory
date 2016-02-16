# Hash table tests

import unittest
from hash_table import HashTable

class TestHashTable(unittest.TestCase):

    def setUp(self):
        self.hash_table = HashTable(13)

    def test_init(self):
        bucket_size = len(self.hash_table.buckets)
        self.assertEqual(13, bucket_size)
        self.assertEqual(bucket_size, self.hash_table.bucket_count)
        self.assertEqual(0, self.hash_table.item_count)

    def test_set_value_for_key(self):
        self.hash_table["key"] = "Bob"
        self.assertEqual(1, self.hash_table.item_count)
        self.assertEqual("Bob", self.hash_table["key"])
        self.hash_table["key"] = "Max"
        self.assertEqual("Max", self.hash_table["key"])

    def test_get_value_for_key(self):
        self.hash_table["Bob"] = "male"
        self.hash_table["Bob"] = "alpha male"
        self.hash_table["Alexa"] = "female"
        self.assertNotEqual("male", self.hash_table["Bob"])
        self.assertEqual("alpha male", self.hash_table["Bob"])

    def test_remove_key(self):
        self.hash_table["Bob"] = "male"
        self.assertEqual("male", self.hash_table["Bob"])
        self.assertEqual(1, self.hash_table.item_count)
        del self.hash_table["Bob"]
        self.assertEqual(0, self.hash_table.item_count)
        self.assertIsNone(self.hash_table["Bob"])

    def test_contains(self):
        self.hash_table["Bob"] = "male"
        self.hash_table["Alex"] = "male"
        self.assertTrue("Bob" in self.hash_table)
        self.assertTrue("Alex" in self.hash_table)
        self.assertFalse("Chris" in self.hash_table)

    # test helper methods

    def test_get_bucket_index_for_key(self):
        index = self.hash_table._get_bucket_index_for_key("key")
        self.assertTrue(index < self.hash_table.bucket_count)
        self.assertTrue(isinstance(index, int))


if __name__ == '__main__':
    unittest.main()
