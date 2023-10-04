# simple O(n) solution with 2 lists
# passes testcases and easy to replicate but is not a prod-ready hashmap
class MyHashMap:

    def __init__(self):
        self.keys = []
        self.values = []
        self.keyset = set()
        

    def put(self, key: int, value: int) -> None:
        if key not in self.keyset:
            self.keys.append(key)
            self.values.append(value)
            self.keyset.add(key)
        else:
            idx = self.keys.index(key)
            self.values[idx] = value
        

    def get(self, key: int) -> int:
        if key not in self.keyset:
            return -1
        else:
            idx = self.keys.index(key)
            return self.values[idx]
        

    def remove(self, key: int) -> None:
        if key in self.keyset:
            idx = self.keys.index(key)
            
            self.keyset.remove(key)
            self.keys.remove(key)
            self.values.pop(idx)

