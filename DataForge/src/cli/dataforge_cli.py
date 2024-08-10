import sys
import os

# Add the src directory to the module search path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from query.query_processor import QueryProcessor

def main(query):
    processor = QueryProcessor()
    result = processor.execute_query(query)
    print(result)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python dataforge_cli.py \"<SQL_QUERY>\"")
        sys.exit(1)
    main(sys.argv[1])
