# src/logging/wal.py
import os

class WriteAheadLog:
    LOG_FILE = "wal.log"

    def __init__(self):
        if not os.path.exists(self.LOG_FILE):
            open(self.LOG_FILE, 'w').close()

    def write(self, entry):
        with open(self.LOG_FILE, 'a') as f:
            f.write(entry + "\n")

    def read(self):
        with open(self.LOG_FILE, 'r') as f:
            return f.readlines()
