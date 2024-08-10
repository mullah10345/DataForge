# tests/unit/test_load_balancer.py
import unittest
from src.core.load_balancer import LoadBalancer

class MockServer:
    def __init__(self, name):
        self.name = name

    def execute_query(self, query):
        return f"Executed {query} on {self.name}"

class TestLoadBalancer(unittest.TestCase):
    def setUp(self):
        self.servers = [MockServer(f"Server{i}") for i in range(3)]
        self.load_balancer = LoadBalancer(self.servers)

    def test_balance_load(self):
        query = "SELECT * FROM table"
        results = [self.load_balancer.balance_load(query) for _ in range(3)]
        expected = [
            "Executed SELECT * FROM table on Server0",
            "Executed SELECT * FROM table on Server1",
            "Executed SELECT * FROM table on Server2"
        ]
        self.assertEqual(results, expected)

if __name__ == '__main__':
    unittest.main()
