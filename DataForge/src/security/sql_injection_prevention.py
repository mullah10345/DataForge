# src/security/sql_injection_prevention.py

class SQLInjectionPrevention:
    def sanitize_input(self, input_string):
        # Replace dangerous characters with safe ones
        return input_string.replace("'", "''").replace(";", "")

    def validate_query(self, query):
        # Basic validation to check for malicious patterns
        if any(keyword in query.lower() for keyword in ["drop", "delete", "--"]):
            raise ValueError("Potential SQL Injection detected")
        return query
