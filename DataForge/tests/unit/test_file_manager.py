# tests/unit/test_file_manager.py
import unittest
import os
from src.storage.file_manager import FileManager

class TestFileManager(unittest.TestCase):
    def setUp(self):
        self.file_manager = FileManager('test_files')
        self.test_file = 'test_file.txt'
        self.test_data = 'Sample data'

    def test_write_and_read_file(self):
        self.file_manager.write_file(self.test_file, self.test_data)
        read_data = self.file_manager.read_file(self.test_file)
        self.assertEqual(read_data, self.test_data)

    def test_delete_file(self):
        self.file_manager.write_file(self.test_file, self.test_data)
        self.file_manager.delete_file(self.test_file)
        self.assertFalse(os.path.exists(self.file_manager._get_file_path(self.test_file)))

    def tearDown(self):
        if os.path.exists('test_files'):
            for file in os.listdir('test_files'):
                os.remove(os.path.join('test_files', file))
            os.rmdir('test_files')

if __name__ == '__main__':
    unittest.main()
