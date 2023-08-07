# board is very small => construnct all possible paths as string
# works, TLE
# optimization needed
# time: O(n*m)^2?
# space: O(n*m)^2
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        paths = set()

        for r in range(len(board)):
            for c in range(len(board[0])):
                visited = set()
                path = []
                self.explore(board, r, c, len(word) - 1, path, paths, visited)
        
        for p in paths:
            if word in "".join(p):
                return True
        
        return False
        

    def explore(self, board, r, c, steps, path, paths, visited):
        visited.add((r, c))
        path.append(board[r][c])

        for nr, nc in self.neighbors(board, r, c):
            if (nr, nc) not in visited:
                self.explore(board, nr, nc, steps - 1, path, paths, visited)
        
        if steps == 0: # base case
            paths.add(tuple(path[:]))

        path.pop()
        visited.remove((r, c))


    def in_bounds(self, board, r, c):
        return 0 <= r < len(board) and 0 <= c < len(board[0])


    def neighbors(self, board, r, c):
        neighbors = []
        if self.in_bounds(board, r, c - 1):
            neighbors.append((r, c - 1))
        if self.in_bounds(board, r, c + 1):
            neighbors.append((r, c + 1))
        if self.in_bounds(board, r - 1, c):
            neighbors.append((r - 1, c))
        if self.in_bounds(board, r + 1, c):
            neighbors.append((r + 1, c))

        return neighbors
