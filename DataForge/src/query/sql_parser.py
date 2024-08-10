import re

class SQLParser:
    def __init__(self):
        self.commands = {
            "CREATE TABLE": self.parse_create_table,
            "INSERT INTO": self.parse_insert,
            "SELECT": self.parse_select,
        }

    def parse(self, query):
        for command in self.commands:
            if query.upper().startswith(command):
                return self.commands[command](query)
        raise ValueError(f"Unknown SQL command: {query}")

    def parse_create_table(self, query):
        match = re.match(r"CREATE TABLE (\w+)\s*\((.+)\)", query, re.IGNORECASE)
        if not match:
            raise ValueError(f"Invalid CREATE TABLE query: {query}")
        table_name = match.group(1)
        columns = [col.strip() for col in match.group(2).split(",")]
        return {"action": "create_table", "table_name": table_name, "columns": columns}

    def parse_insert(self, query):
        match = re.match(r"INSERT INTO (\w+)\s*\((.+)\)\s*VALUES\s*\((.+)\)", query, re.IGNORECASE)
        if not match:
            raise ValueError(f"Invalid INSERT query: {query}")
        table_name = match.group(1)
        columns = [col.strip() for col in match.group(2).split(",")]
        values = [int(val.strip()) for val in match.group(3).split(",")]
        return {"action": "insert", "table_name": table_name, "columns": columns, "values": values}

    def parse_select(self, query):
        match = re.match(r"SELECT (.+) FROM (\w+)\s*(WHERE (.+))?", query, re.IGNORECASE)
        if not match:
            raise ValueError(f"Invalid SELECT query: {query}")
        columns = [col.strip() for col in match.group(1).split(",")]
        table_name = match.group(2)
        where_clause = match.group(4) if match.group(4) else None
        return {"action": "select", "columns": columns, "table_name": table_name, "where": where_clause}
