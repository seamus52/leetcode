from collections import Counter 
class Solution:
    def triangleType(self, nums: List[int]) -> str:
        c = Counter(nums)

        if nums[0] + nums[1] <= nums[2] or nums[1] + nums[2] <= nums[0] or nums[0] + nums[2] <= nums[1]:
            return "none"

        if len(c) == 3:
            return "scalene"
        elif len(c) == 2:
            return "isosceles"
        elif len(c) == 1:
            return "equilateral"

