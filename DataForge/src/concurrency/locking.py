# src/concurrency/locking.py
from threading import Lock

class LockManager:
    def __init__(self):
        self.locks = {}

    def acquire_lock(self, resource_id):
        if resource_id not in self.locks:
            self.locks[resource_id] = Lock()
        self.locks[resource_id].acquire()

    def release_lock(self, resource_id):
        if resource_id in self.locks:
            self.locks[resource_id].release()
