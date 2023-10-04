class MyHashMap:

    def __init__(self):
        self.keyspace = 2017
        self.buckets = [[]] * self.keyspace

    def h(self, key):
        return key % self.keyspace
        
    def put(self, key: int, value: int) -> None:
        hashkey = self.h(key)
        old_item = None
        for i, item in enumerate(self.buckets[hashkey]):
            if item[0] == key:
                old_item = item
                break
        
        if old_item:
            self.buckets[hashkey].remove(old_item)

        self.buckets[hashkey].append((key, value))
        
    def get(self, key: int) -> int:
        hashkey = self.h(key)
        for i, item in enumerate(self.buckets[hashkey]):
            if item[0] == key:
                return item[1]
        return -1
        
    def remove(self, key: int) -> None:
        hashkey = self.h(key)
        item_to_delete = None
        for i, item in enumerate(self.buckets[hashkey]):
            if item[0] == key:
                item_to_delete = item
                break
        
        if item_to_delete:
            self.buckets[hashkey].remove(item_to_delete)
