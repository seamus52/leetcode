# brute force
# time: O(n^3)
# space: O(1)
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        for l in range(len(heights)):
            for r in range(l, len(heights)):
                h = min(heights[l:r + 1])
                w = r - l + 1
                max_area = max(max_area, h * w)

        return max_area
