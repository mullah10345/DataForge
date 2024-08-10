# tests/unit/test_cache_manager.py
import unittest
from src.caching.cache_manager import CacheManager

class TestCacheManager(unittest.TestCase):
    def setUp(self):
        self.cache = CacheManager(capacity=2)

    def test_put_and_get(self):
        self.cache.put("key1", "value1")
        self.assertEqual(self.cache.get("key1"), "value1")

    def test_cache_eviction(self):
        self.cache.put("key1", "value1")
        self.cache.put("key2", "value2")
        self.cache.put("key3", "value3")  # This should evict "key1"
        self.assertIsNone(self.cache.get("key1"))
        self.assertEqual(self.cache.get("key2"), "value2")
        self.assertEqual(self.cache.get("key3"), "value3")

    def tearDown(self):
        self.cache.clear()

if __name__ == '__main__':
    unittest.main()
