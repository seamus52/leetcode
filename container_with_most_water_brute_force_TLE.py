# water = min(height[i], height[j]) * abs(i - j)
# looking for max water
# brute-force naive solution looks simple to build
# However, 10^5 input size suggests that this is insufficient => TLE
# optimization idea: exclude cases (eg all lower between 2 relative tall boundaries), eg, leverage that j comes after i, do not retest everything from 0
# time: O(n^2)
# space: O(1)

class Solution:

    def maxArea(self, height: List[int]) -> int:
        max_w = 0
        for i in range(len(height)):
            for j in range(i + 1, len(height)):
                w = min(height[i], height[j]) * abs(i - j)
                max_w = max(w, max_w)

        return max_w

