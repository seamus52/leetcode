# looks like timestaps always come in order
# => data structure is dict of SortedDicts
# + use bisect.left: find index of greatest value smaller than n
# time: O(log n)
# space: O(n) + overhead of dict implementations
from bisect import bisect_left
from sortedcontainers import SortedDict
class TimeMap:
    def __init__(self):
        self.hashmap = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.hashmap:
            self.hashmap[key] = SortedDict()
        self.hashmap[key][timestamp] = value
        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.hashmap:
            return ""
    
        if timestamp in self.hashmap[key].keys():
            return self.hashmap[key][timestamp]
        else:
            idx_of_effective_ts = bisect_left(self.hashmap[key].keys(), timestamp)
            if not idx_of_effective_ts:
                return ""
            else:
                effective_ts = self.hashmap[key].keys()[idx_of_effective_ts - 1]
                return self.hashmap[key][effective_ts]

            
# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
