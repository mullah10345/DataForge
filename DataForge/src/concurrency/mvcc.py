# src/concurrency/mvcc.py
from collections import defaultdict

class MVCCManager:
    def __init__(self):
        self.versioned_data = defaultdict(lambda: {"version": 0, "data": {}})
        self.transaction_versions = {}

    def read(self, resource_id, transaction_id):
        if transaction_id not in self.transaction_versions:
            self.transaction_versions[transaction_id] = {}
        version = self.versioned_data[resource_id]["version"]
        return self.versioned_data[resource_id]["data"].get(version, None)

    def write(self, resource_id, transaction_id, data):
        if transaction_id not in self.transaction_versions:
            self.transaction_versions[transaction_id] = {}
        current_version = self.versioned_data[resource_id]["version"]
        self.versioned_data[resource_id]["version"] += 1
        new_version = self.versioned_data[resource_id]["version"]
        self.versioned_data[resource_id]["data"][new_version] = data
        self.transaction_versions[transaction_id][resource_id] = new_version
