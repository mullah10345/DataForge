import os
import pickle

class BTreeIndex:
    def __init__(self):
        self.tree = {}

    def insert(self, key, value):
        self.tree[key] = value

    def search(self, key):
        return self.tree.get(key, None)

    def delete(self, key):
        if key in self.tree:
            del self.tree[key]

class HashIndex:
    def __init__(self):
        self.index = {}

    def insert(self, key, value):
        hash_key = hash(key)
        self.index[hash_key] = value

    def search(self, key):
        hash_key = hash(key)
        return self.index.get(hash_key, None)

    def delete(self, key):
        hash_key = hash(key)
        if hash_key in self.index:
            del self.index[hash_key]

class IndexManager:
    def __init__(self, index_dir="indexes"):
        self.index_dir = index_dir
        if not os.path.exists(self.index_dir):
            os.makedirs(self.index_dir)
        self.indexes = {}

    def create_btree_index(self, table_name):
        index = BTreeIndex()
        self.indexes[table_name] = index
        self.save_index(table_name, index)
        return index

    def create_hash_index(self, table_name):
        index = HashIndex()
        self.indexes[table_name] = index
        self.save_index(table_name, index)
        return index

    def get_index(self, table_name):
        if table_name in self.indexes:
            return self.indexes[table_name]
        index = self.load_index(table_name)
        self.indexes[table_name] = index
        return index

    def save_index(self, table_name, index):
        index_path = os.path.join(self.index_dir, f"{table_name}.idx")
        with open(index_path, "wb") as f:
            pickle.dump(index, f)

    def load_index(self, table_name):
        index_path = os.path.join(self.index_dir, f"{table_name}.idx")
        if not os.path.exists(index_path):
            raise FileNotFoundError(f"Index for table {table_name} does not exist.")
        with open(index_path, "rb") as f:
            return pickle.load(f)
