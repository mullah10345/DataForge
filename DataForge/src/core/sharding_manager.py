# src/core/sharding_manager.py

class ShardingManager:
    def __init__(self, shards):
        self.shards = shards

    def get_shard(self, key):
        return self.shards[hash(key) % len(self.shards)]

    def shard_data(self, data):
        sharded_data = {}
        for key, value in data.items():
            shard = self.get_shard(key)
            if shard not in sharded_data:
                sharded_data[shard] = {}
            sharded_data[shard][key] = value
        return sharded_data

    def query_shard(self, key, query):
        shard = self.get_shard(key)
        return shard.execute_query(query)
