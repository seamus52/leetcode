# brute force
# time: O(n^3)
# space: O(1)
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0

        for i in range(len(heights)):
            for j in range(i, len(heights)):
                min_height = min(heights[i:j + 1])  # height between indexes can be lower than at either index
                area = min_height * (abs(i - j) + 1)
                max_area = max(area, max_area)

        return max_area
