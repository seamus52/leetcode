class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        @lru_cache(maxsize=None)
        def dfs(start, remain):
            if remain < 0 or start == len(nums):
                return False

            if remain == 0:
                return True

            for i in range(start + 1, len(nums)):
                if dfs(i, remain - nums[i]):
                    return True

            return False


        s = sum(nums) 
        if s % 2 != 0:
            return False

        return dfs(0, s // 2)

