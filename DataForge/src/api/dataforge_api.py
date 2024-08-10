# src/api/dataforge_api.py
from flask import Flask, request, jsonify
from src.query.query_processor import QueryProcessor

app = Flask(__name__)

# Placeholder for QueryProcessor initialization
query_processor = QueryProcessor(servers=[], shards=[])

@app.route('/query', methods=['POST'])
def execute_query():
    query = request.json.get('query')
    result = query_processor.execute_query(query)
    return jsonify({"result": result})

@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({"status": "healthy"})

if __name__ == "__main__":
    app.run(debug=True)
