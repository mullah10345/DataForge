# tests/unit/test_locking.py
import unittest
from src.concurrency.locking import LockManager

class TestLockManager(unittest.TestCase):
    def setUp(self):
        self.manager = LockManager()
        self.resource_id = "resource_001"

    def test_acquire_lock(self):
        self.manager.acquire_lock(self.resource_id)
        # Verify that the lock is acquired
        self.assertTrue(self.manager.locks[self.resource_id].locked())

    def test_release_lock(self):
        self.manager.acquire_lock(self.resource_id)
        self.manager.release_lock(self.resource_id)
        # Verify that the lock is released
        self.assertFalse(self.manager.locks[self.resource_id].locked())

    def tearDown(self):
        # Clean up resources after tests
        pass

if __name__ == '__main__':
    unittest.main()
