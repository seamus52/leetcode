# time: O(n)
# space: O(n)
# trick:
# 1) notice 2 distinct cases: input has 0, inout does not have 0
# 2) x / y = x * (y ** -1) -> avoid division
# 3) omit current from array: a[:i]) * a[i+1:]
from math import prod
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [0] * len(nums)

        if 0 in nums:
            for i, n in enumerate(nums):
                if n == 0:  # n != 0 case is covered by output initialization
                    output[i] = prod(nums[:i] + nums[i + 1:])
        else:
            p = prod(nums)
            for i, n in enumerate(nums):
                output[i] = int(p * n ** -1)

        return output
