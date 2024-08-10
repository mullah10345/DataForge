# tests/unit/test_wal.py
import unittest
from src.logging.wal import WriteAheadLog

class TestWriteAheadLog(unittest.TestCase):
    def setUp(self):
        self.wal = WriteAheadLog()

    def test_write_log(self):
        self.wal.write("Test log entry")
        logs = self.wal.read()
        self.assertIn("Test log entry", logs)

    def tearDown(self):
        # Clean up log file after tests
        os.remove(self.wal.LOG_FILE)

if __name__ == '__main__':
    unittest.main()
