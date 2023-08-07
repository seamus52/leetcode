# utilizing that dicts preserve insertion order from python 3.7
# trick: every buffer touch (insert/update/read) needs to move the content to the 'front'
# time: O(1)
# space: O(n)
class LRUCache:
    def __init__(self, capacity: int):
        self.data = {}
        self.capacity = capacity
        
    def get(self, key: int) -> int:
        if key in self.data:
            value = self.data[key]
            del self.data[key] # remove
            self.data[key] = value # reinsert at front
            # print(f"state after GET {key}: {self.data}")
            return self.data[key]
        else:
            # print(f"state after GET {key}: {self.data}")
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.data:
            del self.data[key] # remove
        self.data[key] = value # reinsert at front
        if len(self.data.keys()) > self.capacity:
            del self.data[list(self.data.keys())[0]] # list semantics needed for indexability
        # print(f"state after PUT {key} -> {value}: {self.data}")
                
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
