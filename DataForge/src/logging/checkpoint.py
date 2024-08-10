# src/logging/checkpoint.py
import os

class CheckpointManager:
    CHECKPOINT_FILE = "checkpoint.ckpt"

    def __init__(self):
        if not os.path.exists(self.CHECKPOINT_FILE):
            open(self.CHECKPOINT_FILE, 'w').close()

    def create_checkpoint(self, data):
        with open(self.CHECKPOINT_FILE, 'w') as f:
            f.write(data)

    def load_checkpoint(self):
        with open(self.CHECKPOINT_FILE, 'r') as f:
            return f.read()
