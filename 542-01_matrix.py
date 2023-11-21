# create a dist matrix with matching size
# initialize with 0 at 0's in original, everything else inf
# explore mat w/ BFS, update dist[r][c] if d from closest_0 < dist[r][c]
# time: O(v*e)
# space: O(n)
from collections import deque
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        def in_bounds(r, c):
            return 0 <= r < len(mat) and 0 <= c < len(mat[0])

        def neighbors(r, c):
            nbrs = []
            if in_bounds(r - 1, c): nbrs.append((r - 1, c))
            if in_bounds(r + 1, c): nbrs.append((r + 1, c))
            if in_bounds(r, c - 1): nbrs.append((r, c - 1))
            if in_bounds(r, c + 1): nbrs.append((r, c + 1))
            return nbrs

        dist = mat[:]
        q = deque()
        for r in range(len(mat)):
            for c in range(len(mat[0])):
                if mat[r][c] == 0:
                    q.append((r, c))
                else:
                    dist[r][c] = inf

        while q:
            r, c = q.popleft()
            for nr, nc in neighbors(r, c):
                if dist[nr][nc] > dist[r][c] + 1:
                    dist[nr][nc] = dist[r][c] + 1
                    # put back changed cell for reevaluation from other cells
                    q.append((nr, nc))

        return dist

