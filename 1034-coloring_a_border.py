# border: < 4 neighbors
class Solution:
    def colorBorder(self, grid: List[List[int]], row: int, col: int, color: int) -> List[List[int]]:
        def in_bounds(r, c):
            return 0 <= r < len(grid) and 0 <= c < len(grid[0])


        def neighbors(r, c):
            nbrs = []
            if in_bounds(r - 1, c) and grid[r - 1][c] == orig_color:
                nbrs.append((r - 1, c))
            if in_bounds(r + 1, c) and grid[r + 1][c] == orig_color:
                nbrs.append((r + 1, c))
            if in_bounds(r, c - 1) and grid[r][c - 1] == orig_color:
                nbrs.append((r, c - 1))
            if in_bounds(r, c + 1) and grid[r][c + 1] == orig_color:
                nbrs.append((r, c + 1))
            return nbrs


        def explore(r, c):
            if (r, c) in visited:
                return

            visited.add((r, c))

            nbrs = neighbors(r, c)
            if len(nbrs) < 4:
                border.add((r, c))

            for nr, nc in nbrs:
                explore(nr, nc)

        orig_color = grid[row][col]
        visited = set()
        border = set()

        explore(row, col)

        for r, c in border:
            grid[r][c] = color

        return grid
