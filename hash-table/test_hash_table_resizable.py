# Hash table tests

import unittest
from hash_table_resizable import HashTable

class TestHashTable(unittest.TestCase):

    def setUp(self):
        self.hash_table = HashTable(13)

    def test_init(self):
        bucket_size = len(self.hash_table.buckets)
        self.assertEqual(13, bucket_size)
        self.assertEqual(0, self.hash_table.item_count)

    def test_set_item(self):
        self.hash_table["city"] = "San Francisco"
        self.hash_table["state"] = "California"
        self.assertEqual(2, self.hash_table.item_count)

    def test_set_with_same_key(self):
        self.hash_table["city"] = "San Francisco"
        self.hash_table["city"] = "Los Angeles"
        self.hash_table["city"] = "San Bernardino"
        self.assertEqual(1, self.hash_table.item_count)
        self.assertEqual("San Bernardino", self.hash_table["city"])

    def test_set_to_resize_buckets(self):
        for i in range(0, 16):
            self.hash_table["item{}".format(i)] = "Value"
        self.assertEqual(26, len(self.hash_table.buckets))
        self.assertTrue(self.hash_table._load_factor() < 0.8)

    def test_get_item(self):
        self.hash_table["city"] = "San Francisco"
        self.assertEqual(1, self.hash_table.item_count)
        self.assertEqual("San Francisco", self.hash_table["city"])

    def test_get_item_with_nonexisting_key(self):
        self.hash_table["city"] = "San Francisco"
        self.assertIsNone(self.hash_table["state"])

    def test_delete_item(self):
        self.hash_table["city"] = "San Francisco"
        self.assertEqual(1, self.hash_table.item_count)
        del self.hash_table["city"]
        self.assertEqual(0, self.hash_table.item_count)

    def test_delete_item_with_nonexisting_key(self):
        self.assertFalse("city" in self.hash_table)
        with self.assertRaises(KeyError):
            del self.hash_table["city"]

    def test_contains(self):
        self.hash_table["city"] = "San Francisco"
        self.hash_table["country"] = "United States"
        self.assertTrue("city" in self.hash_table)
        self.assertTrue("country" in self.hash_table)
        self.assertFalse("state" in self.hash_table)

if __name__ == '__main__':
    unittest.main()
