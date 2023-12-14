# looks like timestaps always come in order
# + use bisect.left: find index of greatest value smaller than n
# time: O(log n)
# space: O(n) + overhead of dict implementations
from bisect import bisect_left
class TimeMap:

    def __init__(self):
        self.tm_key = {}
        self.tm_ts = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.tm_key.setdefault(key, {})
        self.tm_key[key][timestamp] = value

        self.tm_ts.setdefault(key, [])
        self.tm_ts[key].append(timestamp)

    def get(self, key: str, timestamp: int) -> str:
        # terminate early for non-existing key
        if key not in self.tm_key:
            return ""

        # if timestamp is in hash, access value directly
        if timestamp in self.tm_key[key]:
           return  self.tm_key[key][timestamp]

        # determine effective timestamp: timestamps are naturally ordered
        idx = bisect_left(list(self.tm_ts[key]), timestamp)
        effective_ts = self.tm_ts[key][idx - 1]

        # ensure effective timestamp points to an existing hash bucket
        if effective_ts <= timestamp:
            return self.tm_key[key][effective_ts]

        return ""


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
