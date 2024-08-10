# src/query/query_processor.py

from .sql_parser import SQLParser
from .query_optimizer import QueryOptimizer
from .query_executor import QueryExecutor
from src.caching.cache_manager import CacheManager
from src.security.sql_injection_prevention import SQLInjectionPrevention
from src.security.audit_logger import AuditLogger
from src.core.load_balancer import LoadBalancer
from src.core.sharding_manager import ShardingManager
from src.core.performance_monitor import PerformanceMonitor

class QueryProcessor:
    def __init__(self, servers=None, shards=None):
        # Initialize components
        self.parser = SQLParser()
        self.optimizer = QueryOptimizer()
        self.executor = QueryExecutor()
        self.cache = CacheManager(capacity=100)  # Adjust capacity as needed
        self.sql_injection_prevention = SQLInjectionPrevention()
        self.audit_logger = AuditLogger()
        self.load_balancer = LoadBalancer(servers) if servers else None
        self.sharding_manager = ShardingManager(shards) if shards else None
        self.performance_monitor = PerformanceMonitor()

    def execute_query(self, query, key=None):
        # Sanitize and validate the query
        sanitized_query = self.sql_injection_prevention.sanitize_input(query)
        validated_query = self.sql_injection_prevention.validate_query(sanitized_query)

        # Log the query execution
        self.audit_logger.log(f"Executing query: {validated_query}")

        # Check if the result is in the cache
        cached_result = self.cache.get(validated_query)
        if cached_result is not None:
            return cached_result

        # Parse, optimize, and execute the query
        parsed_query = self.parser.parse(validated_query)
        optimized_query = self.optimizer.optimize(parsed_query)

        # Handle load balancing and sharding if applicable
        if self.load_balancer:
            if key:
                result = self.sharding_manager.query_shard(key, optimized_query)
            else:
                result = self.load_balancer.balance_load(optimized_query)
        else:
            result = self.executor.execute(optimized_query)

        # Store the result in the cache
        self.cache.put(validated_query, result)

        # Monitor query performance
        return self.performance_monitor.monitor_query(optimized_query, lambda q: result)
