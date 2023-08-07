# time: O(n)
# space: O(1)
# Kadane's Algorithm

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        local_max = float("-inf")
        global_max = float("-inf")

        for n in nums:
            local_max = max(n, n + local_max)
            global_max = max(global_max, local_max)

        return global_max
