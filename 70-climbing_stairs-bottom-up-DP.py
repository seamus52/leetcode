# in effect this is a 0-indexed Fibonacci sequence
# time: O(n) - efficient deduplication
# space: O(n) - recursive call depth
from functools import lru_cache
class Solution:
    def climbStairs(self, n: int) -> int:
        @lru_cache(maxsize=None)
        def climb(start):
            if start == n:
                return 1
            
            if start > n:
                return 0

            return climb(start + 1) + climb(start + 2)

        return climb(0)

