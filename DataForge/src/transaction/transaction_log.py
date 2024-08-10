# src/transaction/transaction_log.py
import os

class TransactionLog:
    LOG_FILE = "transaction.log"

    def __init__(self):
        if not os.path.exists(self.LOG_FILE):
            open(self.LOG_FILE, 'w').close()

    def start(self, transaction_id):
        with open(self.LOG_FILE, 'a') as f:
            f.write(f"START {transaction_id}\n")

    def commit(self, transaction_id):
        with open(self.LOG_FILE, 'a') as f:
            f.write(f"COMMIT {transaction_id}\n")

    def rollback(self, transaction_id):
        with open(self.LOG_FILE, 'a') as f:
            f.write(f"ROLLBACK {transaction_id}\n")
