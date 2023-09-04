# time: O(m*n)
# space: O(1)

class Solution:
    def maximalSquare(self, m: List[List[str]]) -> int:
        rows = len(m)
        cols = len(m[0])
        max_side = 0

        for r in range(rows):
            for c in range(cols):
                m[r][c] = int(m[r][c])

                if r - 1 >= 0 and c - 1 >= 0 and m[r][c] > 0:
                    # min ensures to pick the smaller side for calculation
                    m[r][c] += min(m[r - 1][c], m[r][c - 1], m[r - 1][c - 1])
                max_side = max(max_side, m[r][c])

        return max_side ** 2
