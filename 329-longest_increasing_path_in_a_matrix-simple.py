# time: O(n)-ish
# space: O(n)
# memoizing all the functions will prevent TLE
class Solution:
    def longestIncreasingPath(self, m: List[List[int]]) -> int:
        @lru_cache(maxsize=None)
        def in_bounds(r, c):
            return 0 <= r < len(m) and 0 <= c < len(m[0])

        @lru_cache(maxsize=None)
        def neighbors(r, c):
            nbrs = []
            if in_bounds(r - 1, c) and m[r - 1][c] > m[r][c]: nbrs.append((r - 1, c))
            if in_bounds(r + 1, c) and m[r + 1][c] > m[r][c]: nbrs.append((r + 1, c))
            if in_bounds(r, c - 1) and m[r][c - 1] > m[r][c]: nbrs.append((r, c - 1))
            if in_bounds(r, c + 1) and m[r][c + 1] > m[r][c]: nbrs.append((r, c + 1))
            return nbrs

        @lru_cache(maxsize=None)
        def dfs(r, c, dist):
            nonlocal longest_path
            longest_path = max(dist, longest_path)

            for nr, nc in neighbors(r, c):
                dfs(nr, nc, dist + 1)

        longest_path = 0
        for r in range(len(m)):
            for c in range(len(m[0])):
                dfs(r, c, 0)

        return longest_path + 1

