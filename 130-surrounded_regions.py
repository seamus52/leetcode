# cell is surrounded if there is no path to border
# rewrite:
# - From each border 'O'
# - BFS, mark all nodes as E
# - mark all O as X
# - mark all E as O

from collections import deque
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        def in_bounds(r, c):
            return 0 <= r < len(board) and 0 <= c < len(board[0])

        def is_border(r, c):
            r_border = [0, len(board) - 1]
            c_border = [0, len(board[0]) - 1]
            return r in r_border or c in c_border

        # also filters on 'O' cell value
        def neighbors(r, c):
            nbrs = []
            if in_bounds(r - 1, c) and board[r - 1][c] != 'X':
                nbrs.append((r - 1, c))
            if in_bounds(r + 1, c) and board[r + 1][c] != 'X':
                nbrs.append((r + 1, c))
            if in_bounds(r, c - 1) and board[r][c - 1] != 'X':
                nbrs.append((r, c - 1))
            if in_bounds(r, c + 1) and board[r][c + 1] != 'X':
                nbrs.append((r, c + 1))
            return nbrs

        def dfs(r, c, visited):
            visited.add((r, c))
            board[r][c] = 'E'

            for nr, nc in neighbors(r, c):
                if (nr, nc) not in visited:
                    dfs(nr, nc, visited)

        border_nodes = []
        for r in range(len(board)):
            for c in range(len(board[0])):
                if is_border(r, c) and board[r][c] == 'O':
                    border_nodes.append((r, c))

        for r, c in border_nodes:
            visited = set()
            dfs(r, c, visited)

        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == 'O':
                    board[r][c] = 'X'

        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == 'E':
                    board[r][c] = 'O'
