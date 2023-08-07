# create a dist matrix with matching size
# initialize with 0 at 0's in original, everything else inf
# explore mat w/ BFS, update dist[r][c] if d from closest_0 < dist[r][c]
# time: O(v*e)
# space: O(n)

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        def in_bounds(mat, r, c):
            return 0 <= r < len(mat) and 0 <= c < len(mat[0])

        def neighbors(mat, r, c):
            neighbors = []
            if in_bounds(mat, r - 1, c): neighbors.append((r - 1, c))
            if in_bounds(mat, r + 1, c): neighbors.append((r + 1, c))
            if in_bounds(mat, r, c - 1): neighbors.append((r, c - 1))
            if in_bounds(mat, r, c + 1): neighbors.append((r, c + 1))
            return neighbors

        q = deque()

        dist = []
        for r in range(len(mat)):
            dist.append([])
            for c in range(len(mat[0])):
                value = 0 if mat[r][c] == 0 else float("inf")
                dist[r].append(value)
                if value == 0:
                    q.append((r, c, 0))

        visited = set()
        while q:
            r, c, d = q.popleft()
            if d == 0: visited = set()
            visited.add((r, c))

            if dist[r][c] > 0 and d < dist[r][c]:
                dist[r][c] = d

            for nr, nc in neighbors(dist, r, c):
                if (nr, nc) not in visited:
                    q.append((nr, nc, d + 1))

        return dist

