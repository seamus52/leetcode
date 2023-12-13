# time: O(n) log n
# space: O(n)
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        nums_sorted = sorted(nums)[-2:]
        return (nums_sorted[0] - 1) * (nums_sorted[1] - 1)

