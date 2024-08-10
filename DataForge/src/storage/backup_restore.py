# src/storage/backup_restore.py
import shutil
import os

class BackupManager:
    def __init__(self, base_path):
        self.base_path = base_path

    def backup(self, backup_path):
        shutil.copytree(self.base_path, backup_path)

    def restore(self, backup_path):
        shutil.rmtree(self.base_path, ignore_errors=True)
        shutil.copytree(backup_path, self.base_path)
