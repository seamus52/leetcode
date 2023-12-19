# time: O(n log n)
# space: O(n)
class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        nums_sorted = sorted(nums)
        
        a, b = nums_sorted[-2:]
        c, d = nums_sorted[:2]

        return (a * b) - (c * d)

