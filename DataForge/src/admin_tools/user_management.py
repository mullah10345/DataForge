# src/admin_tools/user_management.py

class UserManagement:
    def __init__(self):
        self.users = {}

    def add_user(self, username, role):
        self.users[username] = {"role": role}
        print(f"User {username} added with role {role}")

    def remove_user(self, username):
        if username in self.users:
            del self.users[username]
            print(f"User {username} removed")
        else:
            print(f"User {username} not found")

    def list_users(self):
        for username, info in self.users.items():
            print(f"{username}: {info['role']}")
