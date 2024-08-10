import os
import struct
from indexing.index_manager import IndexManager

class StorageEngine:
    def __init__(self, data_dir="data", index_dir="indexes"):
        self.data_dir = data_dir
        self.index_manager = IndexManager(index_dir)
        if not os.path.exists(self.data_dir):
            os.makedirs(self.data_dir)

    def create_table(self, table_name):
        table_path = os.path.join(self.data_dir, f"{table_name}.db")
        if os.path.exists(table_path):
            raise FileExistsError(f"Table {table_name} already exists.")
        with open(table_path, "wb") as f:
            pass  # Initialize an empty table file
        self.index_manager.create_btree_index(table_name)  # Create a B-tree index by default

    def insert_record(self, table_name, record):
        table_path = os.path.join(self.data_dir, f"{table_name}.db")
        if not os.path.exists(table_path):
            raise FileNotFoundError(f"Table {table_name} does not exist.")
        with open(table_path, "ab") as f:
            record_pos = f.tell()
            f.write(self.serialize_record(record))
        index = self.index_manager.get_index(table_name)
        index.insert(record[0], record_pos)  # Assume the first element in the record is the key
        self.index_manager.save_index(table_name, index)

    def fetch_record_by_key(self, table_name, key):
        index = self.index_manager.get_index(table_name)
        record_pos = index.search(key)
        if record_pos is None:
            return None
        table_path = os.path.join(self.data_dir, f"{table_name}.db")
        with open(table_path, "rb") as f:
            f.seek(record_pos)
            return self.deserialize_record(f)

    def serialize_record(self, record):
        return struct.pack("i" * len(record), *record)

    def deserialize_record(self, f):
        record_data = f.read(4 * 3)  # Assuming a record consists of three integers
        if not record_data:
            return None
        return struct.unpack("i" * 3, record_data)
