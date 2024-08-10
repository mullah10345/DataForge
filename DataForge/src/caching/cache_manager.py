# src/caching/cache_manager.py
from collections import OrderedDict

class CacheManager:
    def __init__(self, capacity=100):
        self.cache = OrderedDict()
        self.capacity = capacity

    def get(self, key):
        if key not in self.cache:
            return None
        else:
            # Move the accessed item to the end of the OrderedDict
            value = self.cache.pop(key)
            self.cache[key] = value
            return value

    def put(self, key, value):
        if key in self.cache:
            # Remove the old value
            self.cache.pop(key)
        elif len(self.cache) >= self.capacity:
            # Remove the oldest item (FIFO policy)
            self.cache.popitem(last=False)
        self.cache[key] = value

    def clear(self):
        self.cache.clear()
