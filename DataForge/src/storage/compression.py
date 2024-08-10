# src/storage/compression.py
import zlib

class CompressionManager:
    def compress(self, data):
        return zlib.compress(data.encode())

    def decompress(self, compressed_data):
        return zlib.decompress(compressed_data).decode()
