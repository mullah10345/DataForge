# src/transaction/transaction_manager.py
from src.logging.wal import WriteAheadLog
from src.logging.checkpoint import CheckpointManager
from src.logging.recovery import RecoveryManager

class TransactionManager:
    def __init__(self):
        self.transaction_log = TransactionLog()
        self.isolation = TransactionIsolation()
        self.lock_manager = LockManager()
        self.mvcc_manager = MVCCManager()
        self.wal = WriteAheadLog()
        self.checkpoint = CheckpointManager()
        self.recovery = RecoveryManager()
        self.active_transactions = {}

    def begin_transaction(self, transaction_id):
        if transaction_id in self.active_transactions:
            raise ValueError(f"Transaction {transaction_id} is already active.")
        self.active_transactions[transaction_id] = {'status': 'active'}
        self.transaction_log.start(transaction_id)
        self.wal.write(f"BEGIN {transaction_id}")

    def commit_transaction(self, transaction_id):
        if transaction_id not in self.active_transactions:
            raise ValueError(f"Transaction {transaction_id} does not exist.")
        if self.active_transactions[transaction_id]['status'] != 'active':
            raise ValueError(f"Transaction {transaction_id} is not active.")
        
        self.isolation.validate(transaction_id)
        self.transaction_log.commit(transaction_id)
        self.wal.write(f"COMMIT {transaction_id}")
        self.active_transactions[transaction_id]['status'] = 'committed'

    def rollback_transaction(self, transaction_id):
        if transaction_id not in self.active_transactions:
            raise ValueError(f"Transaction {transaction_id} does not exist.")
        if self.active_transactions[transaction_id]['status'] != 'active':
            raise ValueError(f"Transaction {transaction_id} is not active.")
        
        self.transaction_log.rollback(transaction_id)
        self.wal.write(f"ROLLBACK {transaction_id}")
        self.active_transactions[transaction_id]['status'] = 'rolled_back'
        del self.active_transactions[transaction_id]

    def create_checkpoint(self, data):
        self.checkpoint.create_checkpoint(data)

    def recover(self):
        return self.recovery.recover()
