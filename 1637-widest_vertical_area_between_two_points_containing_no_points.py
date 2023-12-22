# time: O(n * log n)
# space: O(n)
class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        p = sorted([x[0] for x in points])
        max_d = 0

        for i in range(1, len(p)):
            d = p[i] - p[i - 1]
            max_d = max(max_d, d)

        return max_d

