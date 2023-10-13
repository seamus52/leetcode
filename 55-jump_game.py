# time: O(n^2) - For every element, we are looking at the next nums[i] elements to the  right. nums[i] can be at most n (length of array)
# space: O(1)
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        @lru_cache(maxsize=None)
        def traverse(i):
            if i == len(nums) - 1:
                return True

            for step in range(1, nums[i] + 1):
                if traverse(i + step):
                    return True

            return False

        return traverse(0)
