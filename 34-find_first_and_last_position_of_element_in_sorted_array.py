from bisect import bisect_left, bisect_right
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]

        l = bisect_left(nums, target)
        r = bisect_right(nums, target)
        if l == r:
            return [-1, -1]

        return [l, r - 1]
        
