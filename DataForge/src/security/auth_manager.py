# src/security/auth_manager.py
import hashlib

class AuthManager:
    def __init__(self):
        self.users = {}  # Stores username:hashed_password
        self.roles = {}  # Stores username:role

    def hash_password(self, password):
        return hashlib.sha256(password.encode()).hexdigest()

    def add_user(self, username, password, role):
        hashed_password = self.hash_password(password)
        self.users[username] = hashed_password
        self.roles[username] = role

    def authenticate_user(self, username, password):
        hashed_password = self.hash_password(password)
        return self.users.get(username) == hashed_password

    def authorize_user(self, username, required_role):
        return self.roles.get(username) == required_role
