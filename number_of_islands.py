#time: O(n) - cells of grid
#space: O(n) - worst case for visited, also stack frame
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        island_count = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == "1" and (r, c) not in visited:
                    island_count += 1
                    self.traverse(grid, r, c, visited)

        return island_count


    def in_bounds(self, grid, r, c):
        return 0 <= r < len(grid) and 0 <= c < len(grid[0])


    def neighbors(self, grid, r, c):
        neighbors = set()
        if self.in_bounds(grid, r - 1, c):
            neighbors.add((r - 1, c))
        if self.in_bounds(grid, r + 1, c):
            neighbors.add((r + 1, c))
        if self.in_bounds(grid, r, c - 1):
            neighbors.add((r, c - 1))
        if self.in_bounds(grid, r, c + 1):
            neighbors.add((r, c + 1))

        return neighbors


    def traverse(self, grid, r, c, visited):
        if (r, c) in visited:
            return

        visited.add((r, c))
        for nr, nc in self.neighbors(grid, r, c):
            if (nr, nc) not in visited and grid[nr][nc] == "1":
                self.traverse(grid, nr, nc, visited)
