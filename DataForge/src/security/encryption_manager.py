# src/security/encryption_manager.py
from cryptography.fernet import Fernet

class EncryptionManager:
    def __init__(self, key=None):
        self.key = key or Fernet.generate_key()
        self.cipher = Fernet(self.key)

    def encrypt(self, data):
        return self.cipher.encrypt(data.encode())

    def decrypt(self, encrypted_data):
        return self.cipher.decrypt(encrypted_data).decode()

    def get_key(self):
        return self.key
