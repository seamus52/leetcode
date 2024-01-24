from math import prod
class Solution:
    def arraySign(self, nums: List[int]) -> int:
        p = prod(nums)
        if p > 0:
            return 1
        elif p < 0:
            return -1
        
        return 0

