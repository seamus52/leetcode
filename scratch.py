# simple BFS
from collections import deque
def minDistance(height, width, tree, squirrel, nuts) -> int:
    def in_bounds(row, col):
        return (0 <= row < height) and (0 <= col < width)

    def neighbors(row, col):
        nbrs = []
        if in_bounds(row + 1, col):
            nbrs.append((row + 1, col))
        if in_bounds(row - 1, col):
            nbrs.append((row - 1, col))
        if in_bounds(row, col + 1):
            nbrs.append((row, col + 1))
        if in_bounds(row, col - 1):
            nbrs.append((row, col - 1))
        return nbrs

    def bfs(row, col, dest_type):
        nonlocal dist
        q = deque([(row, col, 0)])
        
        while q:
            print(q)
            r, c, steps = q.popleft()
            visited.add((r, c))

            if dest_type == "N" and (r, c) in nuts:
                dist += steps
                nuts.remove((r, c))
                return (r, c)
            if dest_type == "T" and (r, c) == tree:
                dist += steps
                return (r, c)
            
            for (nr, nc) in neighbors(r, c):
                if (nr, nc) not in visited:
                    q.append((nr, nc, steps + 1))

        return (-1, -1) # stopgap: should never get here
            

    squirrel = (squirrel[0], squirrel[1])
    tree = (tree[0], tree[1])
    nuts = set((r, c) for r, c in nuts)
    print(squirrel, tree, nuts)

    dist = 0
    while nuts:
        visited = set()
        squirrel = bfs(squirrel[0], squirrel[1], "N")
        # visited = set()
        # squirrel = bfs(squirrel[0], squirrel[1], "T")

    return dist

print(minDistance(5, 7, [2,2], [4,4], [[3,0], [2,5]]))

