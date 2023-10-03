#time: O(rolw*col)^2
#space: O(1)
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        dist = mat[:]
        
        for r in range(len(mat)):
            for c in range(len(mat[0])):
                dist[r][c] = self.find_closest_zero(mat, r, c)

        return dist

    # brute-force: use BFS
    from collections import deque
    def find_closest_zero(self, mat, row, col):
        q = deque([(row, col, 0)])
        visited = set()

        while q:
            r, c, level = q.popleft()
            visited.add((r, c))
            if mat[r][c] == 0:
                return level
            for nr, nc in self.neighbors(mat, r, c):
                if (nr, nc) not in visited:
                    q.append((nr, nc, level + 1))


    def neighbors(self, mat, r, c):
        neighbors = []
        if self.in_bounds(mat, r - 1, c):
            neighbors.append((r - 1, c))
        if self.in_bounds(mat, r + 1, c):
            neighbors.append((r + 1, c))
        if self.in_bounds(mat, r, c - 1):
            neighbors.append((r, c - 1))
        if self.in_bounds(mat, r, c + 1):
            neighbors.append((r, c + 1))

        return neighbors


    def in_bounds(self, mat, r, c):
        return 0 <= r < len(mat) and 0 <= c < len(mat[0])

