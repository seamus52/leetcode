#simple BFS
# time: O(max(x, y)^2)
# space: O(max(x, y)^2)
class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        def neighbors(r, c):
            neighbors = set()
            neighbors.add((r - 2, c - 1))
            neighbors.add((r - 1, c - 2))
            neighbors.add((r - 2, c + 1))
            neighbors.add((r - 1, c + 2))
            neighbors.add((r + 2, c - 1))
            neighbors.add((r + 1, c - 2))
            neighbors.add((r + 2, c + 1))
            neighbors.add((r + 1, c + 2))
            return neighbors

        def find_path(r, c):
            q = deque([(0, 0, 0)])
            visited = set()

            while q:
                r, c, level = q.popleft()
                if r == y and c == x:
                    return level

                for nr, nc in neighbors(r, c):
                    if (nr, nc) not in visited:
                        q.append((nr, nc, level + 1))
                        visited.add((nr, nc)) # optimization, do this here instead of after popleft
                    
        return find_path(y, x)
