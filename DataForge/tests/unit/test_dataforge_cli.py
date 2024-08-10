# tests/unit/test_dataforge_cli.py
import unittest
from src.cli.dataforge_cli import DataForgeCLI
from src.query.query_processor import QueryProcessor


class MockQueryProcessor(QueryProcessor):
    def execute_query(self, query):
        return f"Executed {query}"

class TestDataForgeCLI(unittest.TestCase):
    def setUp(self):
        self.query_processor = MockQueryProcessor(servers=[], shards=[])
        self.cli = DataForgeCLI(self.query_processor)

    def test_cli_exit(self):
        with self.assertRaises(SystemExit):
            self.cli.start()

if __name__ == '__main__':
    unittest.main()
