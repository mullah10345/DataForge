# src/admin_tools/performance_tuner.py
from src.core.performance_monitor import PerformanceMonitor

class PerformanceTuner:
    def __init__(self, performance_monitor):
        self.performance_monitor = performance_monitor

    def tune_query(self, query):
        # Placeholder for tuning logic
        print(f"Tuning query: {query}")

    def view_performance_metrics(self):
        metrics = self.performance_monitor.get_metrics()
        for metric in metrics:
            print(f"Query: {metric[0]}, Time: {metric[1]}s")
