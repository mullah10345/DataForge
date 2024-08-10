# src/storage/partitioning.py
class PartitionManager:
    def __init__(self, partitions):
        self.partitions = partitions

    def get_partition(self, key):
        return self.partitions[hash(key) % len(self.partitions)]

    def horizontal_partition(self, data):
        # Example of horizontal partitioning
        partitioned_data = {}
        for key, value in data.items():
            partition = self.get_partition(key)
            if partition not in partitioned_data:
                partitioned_data[partition] = {}
            partitioned_data[partition][key] = value
        return partitioned_data

    def vertical_partition(self, data, columns):
        # Example of vertical partitioning
        partitioned_data = {col: {} for col in columns}
        for key, value in data.items():
            for col in columns:
                if col in value:
                    partitioned_data[col][key] = value[col]
        return partitioned_data
