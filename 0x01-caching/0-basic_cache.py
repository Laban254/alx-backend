#!/usr/bin/python3
""" Basic dictionary """
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    def __init__(self):
        super().__init__()

    def put(self, key, item):
        """add item to cache"""

        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """returns the key"""

        if key is not None and key in self.cache_data:
            return self.cache_data.get(key)
        return None
