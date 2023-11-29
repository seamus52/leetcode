#time: O(n*m), process the whole grid
#space: O(n*m) worst case, all oranges need to rot
from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        def count_fresh(grid):
            fresh = 0
            for row in grid:
                fresh += row.count(1)
            return fresh

        def in_bounds(r, c):
            return 0 <= r < len(grid) and 0 <= c < len(grid[0])

        def neighbors(r, c):
            nbrs = []
            if in_bounds(r - 1, c) and grid[r - 1][c] == 1:
                nbrs.append((r - 1, c))
            if in_bounds(r + 1, c) and grid[r + 1][c] == 1:
                nbrs.append((r + 1, c))
            if in_bounds(r, c - 1) and grid[r][c - 1] == 1:
                nbrs.append((r, c - 1))
            if in_bounds(r, c + 1) and grid[r][c + 1] == 1:
                nbrs.append((r, c + 1))
            return nbrs

        # edge case: no fresh oranges in the beginning
        if count_fresh(grid) == 0:
            return 0

        # init
        elapsed = 0
        next_up = []
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 2:
                    for nr, nc in neighbors(r, c):
                        next_up.append((nr, nc))


        while next_up:
            rot_q = next_up[:]
            next_up = []

            # rot the contents of the queue
            for r, c in rot_q:
                grid[r][c] = 2

            # find next round to rot
            for r, c in rot_q:
                for nr, nc in neighbors(r, c):
                    next_up.append((nr, nc))

            elapsed += 1

        # check for unaccessible areas
        if count_fresh(grid) > 0:
            return -1

        return elapsed

