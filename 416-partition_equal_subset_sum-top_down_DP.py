# time: O(sumset sum * len(nums)
# space: O(sumset sum * len(nums)
from functools import lru_cache
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        @lru_cache(maxsize=None)
        def dfs(i, remain):
            if remain == 0:
                return True
            if remain < 0 or i < 0:
                return False

            # inculde or exclude num at current idx
            return dfs(i - 1, remain - nums[i]) or dfs(i - 1, remain)

        s = sum(nums)
        if s % 2 != 0:
            return False

        return dfs(len(nums) - 1, s // 2)

