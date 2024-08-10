# tests/unit/test_transaction_manager.py
import unittest
from src.transaction.transaction_manager import TransactionManager

class TestTransactionManager(unittest.TestCase):
    def setUp(self):
        self.manager = TransactionManager()
        self.transaction_id = "txn_001"

    def test_begin_transaction(self):
        self.manager.begin_transaction(self.transaction_id)
        self.assertEqual(self.manager.active_transactions[self.transaction_id]['status'], 'active')

    def test_commit_transaction(self):
        self.manager.begin_transaction(self.transaction_id)
        self.manager.commit_transaction(self.transaction_id)
        self.assertEqual(self.manager.active_transactions[self.transaction_id]['status'], 'committed')

    def test_rollback_transaction(self):
        self.manager.begin_transaction(self.transaction_id)
        self.manager.rollback_transaction(self.transaction_id)
        self.assertEqual(self.manager.active_transactions[self.transaction_id]['status'], 'rolled_back')

    def tearDown(self):
        # Clean up resources after tests
        pass

if __name__ == '__main__':
    unittest.main()
