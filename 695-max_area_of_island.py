class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def in_bounds(r, c):
            return r in range(len(grid)) and c in range(len(grid[0]))

        def neighbors(r, c):
            nbrs = []
            if in_bounds(r - 1, c) and grid[r - 1][c] == 1: nbrs.append((r - 1, c))
            if in_bounds(r + 1, c) and grid[r + 1][c] == 1: nbrs.append((r + 1, c))
            if in_bounds(r, c - 1) and grid[r][c - 1] == 1: nbrs.append((r, c - 1))
            if in_bounds(r, c + 1) and grid[r][c + 1] == 1: nbrs.append((r, c + 1))
            return nbrs

        def dfs(r, c, visited):
            visited.add((r, c))
            grid[r][c] = 2

            for nr, nc in neighbors(r, c):
                if (nr, nc) not in visited:
                    dfs(nr, nc, visited)

        max_area = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    visited = set()
                    dfs(r, c, visited)
                    max_area = max(max_area, len(visited))

        return max_area

