# time: O(n)
# space: O(n)
# trick:
# 1) notice 2 distinct cases: input has 0, inout does not have 0
# 2) x / y = x * (y ** -1) -> avoid division
# 3) omit current from array: a[:i]) * a[i+1:]
from math import prod
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [0] * len(nums)

        if 0 in nums:
            for i in range(len(nums)):
                if nums[i] == 0:
                    output[i] = prod(nums[:i]) * prod(nums[i+1:])
                else:
                    output[i] = 0
        else:
            list_product = prod(nums)
            for i in range(len(nums)):
                output[i] = int(list_product * (nums[i] ** -1))
            
        return output
