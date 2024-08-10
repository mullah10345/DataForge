# src/storage/file_manager.py
import os

class FileManager:
    def __init__(self, base_path):
        self.base_path = base_path
        if not os.path.exists(base_path):
            os.makedirs(base_path)

    def _get_file_path(self, filename):
        return os.path.join(self.base_path, filename)

    def write_file(self, filename, data):
        with open(self._get_file_path(filename), 'w') as file:
            file.write(data)

    def read_file(self, filename):
        with open(self._get_file_path(filename), 'r') as file:
            return file.read()

    def delete_file(self, filename):
        os.remove(self._get_file_path(filename))
