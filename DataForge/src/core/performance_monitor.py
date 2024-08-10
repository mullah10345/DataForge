# src/core/performance_monitor.py
import time

class PerformanceMonitor:
    def __init__(self):
        self.metrics = []

    def log_query_time(self, query, execution_time):
        self.metrics.append((query, execution_time))

    def monitor_query(self, query, execute_fn):
        start_time = time.time()
        result = execute_fn(query)
        end_time = time.time()
        execution_time = end_time - start_time
        self.log_query_time(query, execution_time)
        return result

    def get_metrics(self):
        return self.metrics
