# time: O(n^2)
# space: O(1)
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        @lru_cache(maxsize=None)
        def traverse(i):
            if i >= len(nums):
                return False

            if i == len(nums) - 1:
                return True

            if nums[i] == 0:
                return False

            for nbr in range(i + 1, i + nums[i] + 1):
                if traverse(nbr):
                    return True

            return False
        
        return traverse(0)
