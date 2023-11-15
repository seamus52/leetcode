# time: O(n)
# space: O(n)-ish
from collections import Counter
class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        c = Counter(arr)
        if len(c.keys()) == 1:
            if 1 in c:
                return 1
            return len(arr)
  
        if set(c.keys()) == set([1, 2]):
            return 2

        for k, v in c.items():
            if k != 1 and v > len(c):
                return k + 1
        
        return len(c)
        
