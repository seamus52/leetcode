# time: O(n log n) - sort dominates
# space: O(n)
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        return sorted([(x ** 2) for x in nums])
