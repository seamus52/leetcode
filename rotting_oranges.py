#time: O(n*m), process thw whole grid
#space: O(n*m) worst case, all oranges need to rot
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = collections.deque()
        fresh_cnt = 0

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    fresh_cnt += 1
                if grid[r][c] == 2:
                    # add starting coordinate for all rotten clusters
                    q.append((r, c))

        if fresh_cnt == 0:
            return 0

        # BFS to rot 1 more layer of oranges around all clusters
        timer = 0
        while q:
            for cluster in range(len(q)): # processes all clusters en every step
                r, c = q.popleft()
                for nr, nc in self.neighbors(grid, r, c):
                    if self.in_bounds(grid, nr, nc) and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        fresh_cnt -= 1
                        q.append((nr,nc))
            timer += 1
        return timer - 1 if fresh_cnt == 0 else -1
            

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


    def in_bounds(self, grid, r, c):
        return 0 <= r < len(grid) and 0 <= c < len(grid[0])
