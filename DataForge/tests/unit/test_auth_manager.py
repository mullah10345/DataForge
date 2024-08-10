# tests/unit/test_auth_manager.py
import unittest
from src.security.auth_manager import AuthManager

class TestAuthManager(unittest.TestCase):
    def setUp(self):
        self.auth_manager = AuthManager()
        self.auth_manager.add_user('user1', 'password1', 'admin')

    def test_authenticate_user(self):
        self.assertTrue(self.auth_manager.authenticate_user('user1', 'password1'))
        self.assertFalse(self.auth_manager.authenticate_user('user1', 'wrongpassword'))

    def test_authorize_user(self):
        self.assertTrue(self.auth_manager.authorize_user('user1', 'admin'))
        self.assertFalse(self.auth_manager.authorize_user('user1', 'user'))

    def tearDown(self):
        self.auth_manager.users.clear()
        self.auth_manager.roles.clear()

if __name__ == '__main__':
    unittest.main()
