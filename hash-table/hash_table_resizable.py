# Hash table implementation

class HashTable:
    """
    An implementation for the hash table data structure
    """

    def __init__(self, bucket_count):
        self.buckets = [None] * bucket_count
        self.item_count = 0

    def __getitem__(self, key):
        bucket_index = self._quadratic_bucket_search(key)
        if bucket_index is None:
            return None
        bucket = self.buckets[bucket_index]
        return bucket[1]

    def __setitem__(self, key, value):
        if self._load_factor() > 0.8:
            self._resize_buckets()
        bucket_count = len(self.buckets)
        bucket_index = self._get_bucket_index_for_key(key)
        bucket = self.buckets[bucket_index]
        if bucket is not None:
            if bucket[0] == key:
                self.buckets[bucket_index] = (key, value)
                return
            count = 0
            while count != bucket_count:
                new_index = (hash(key) + count ** 2) % bucket_count
                bucket = self.buckets[new_index]
                if bucket is None:
                    self.item_count += 1
                    self.buckets[new_index] = (key, value)
                    return
                elif bucket[0] == key:
                    self.buckets[new_index] = (key, value)
                    return
                count += 1
        self.buckets[bucket_index] = (key, value)
        self.item_count += 1

    def __delitem__(self, key):
        bucket_index = self._quadratic_bucket_search(key)
        if bucket_index is None:
            raise KeyError("Key does not exist")
        self.buckets[bucket_index] = None
        self.item_count -= 1

    def __contains__(self, key):
        if not self._quadratic_bucket_search(key):
            return False
        return True

    def __len__(self):
        return self.item_count

    # helper methods

    def _resize_buckets(self):
        self.item_count = 0
        old_buckets = self.buckets
        self.buckets = [None] * len(self.buckets) * 2
        for item in old_buckets:
            if item is not None:
                self.__setitem__(item[0], item[1])

    def _load_factor(self):
        return self.item_count / len(self.buckets)

    def _quadratic_bucket_search(self, key):
        bucket_count = len(self.buckets)
        bucket_index = hash(key) % bucket_count
        bucket = self.buckets[bucket_index]
        if bucket is not None and bucket[0] == key:
            return bucket_index
        count = 0
        while count != bucket_count:
            new_index = (hash(key) + count ** 2) % bucket_count
            bucket = self.buckets[new_index]
            if bucket is not None and bucket[0] == key:
                return bucket_index
            count += 1
        return None

    def _get_bucket_index_for_key(self, key):
        return hash(key) % len(self.buckets)
