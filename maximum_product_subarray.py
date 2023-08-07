# time: O(n)
# space: O(1)
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        local_max = global_max = prev_min = prev_max = nums[0]

        for n in nums[1:]:
            local_min = min(prev_min * n, prev_max * n, n)
            local_max = max(prev_min * n, prev_max * n, n)

            global_max = max(local_max, global_max)
            
            prev_min = local_min
            prev_max = local_max

        return global_max
