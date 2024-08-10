# src/query/query_executor.py

from ..storage.storage_engine import StorageEngine

class QueryExecutor:
    def __init__(self):
        self.storage_engine = StorageEngine()

    def execute(self, optimized_query):
        action = optimized_query.get("action")
        if action == "create_table":
            return self.execute_create_table(optimized_query)
        elif action == "insert":
            return self.execute_insert(optimized_query)
        elif action == "select":
            return self.execute_select(optimized_query)
        else:
            raise ValueError(f"Unknown action: {action}")

    def execute_create_table(self, query):
        table_name = query.get("table_name")
        self.storage_engine.create_table(table_name)
        return f"Table {table_name} created successfully."

    def execute_insert(self, query):
        table_name = query.get("table_name")
        values = query.get("values")
        self.storage_engine.insert_record(table_name, values)
        return f"Record inserted into {table_name}."

    def execute_select(self, query):
        table_name = query.get("table_name")
        where_clause = query.get("where")
        if where_clause:
            key = int(where_clause.split("=")[1].strip())
            record = self.storage_engine.fetch_record_by_key(table_name, key)
            return record if record else "No matching record found."
        else:
            records = self.storage_engine.fetch_records(table_name)
            return records
