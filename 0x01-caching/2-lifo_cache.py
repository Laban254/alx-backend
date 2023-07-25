#!/usr/bin/env python3
"""  FIFO caching """
from typing import Any
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    "FIFO Caching class " ""

    def __init__(self):
        """initialize FIFOCache"""
        super().__init__()
        self.stack = []

    def put(self, key: Any, item: Any) -> None:
        """add an item in the cache"""

        if key is None and item is None:
            return

        if len(self.cache_data) >= self.MAX_ITEMS:
            last_key = self.stack.pop()
            del self.cache_data[last_key]
            print("DISCARD:", last_key)

        self.cache_data[key] = item
        self.stack.append(key)

    def get(self, key: Any) -> Any:
        """retrive an irem rom the cache"""

        if key is None or key not in self.cache_data:
            return None
        return self.cache_data.get(key)
