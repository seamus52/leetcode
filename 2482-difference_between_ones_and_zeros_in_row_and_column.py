# time: O(n * m)
# space: O(n + m)
class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        row_stats = []
        for row in grid:
            row_stats.append((row.count(0), row.count(1)))

        col_stats = []
        for row in zip(*grid):
            col_stats.append((row.count(0), row.count(1)))

        diff = grid[:]
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                grid[r][c] = row_stats[r][1] + col_stats[c][1] - row_stats[r][0] - col_stats[c][0]

        return diff
