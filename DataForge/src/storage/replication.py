# src/storage/replication.py
class ReplicationManager:
    def __init__(self, replicas):
        self.replicas = replicas

    def replicate(self, data):
        for replica in self.replicas:
            replica.write_file("data_replica", data)
