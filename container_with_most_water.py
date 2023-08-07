# water = min(height[i], height[j]) * abs(i - j)
# use 2 ptr
# time: O(1)
# space: O(1)

class Solution:

    def maxArea(self, height: List[int]) -> int:
        i = 0
        j = len(height) - 1
        max_w = 0
        
        while i < j:
            w = min(height[i], height[j]) * abs(i - j)
            max_w = max(w, max_w)
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        
        return max_w
