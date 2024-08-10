# src/core/load_balancer.py

class LoadBalancer:
    def __init__(self, servers):
        self.servers = servers
        self.current_index = 0

    def get_next_server(self):
        server = self.servers[self.current_index]
        self.current_index = (self.current_index + 1) % len(self.servers)
        return server

    def balance_load(self, query):
        server = self.get_next_server()
        return server.execute_query(query)
