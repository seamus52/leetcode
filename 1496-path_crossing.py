# time: O(n)
# space: O(n)
class Solution:
    def isPathCrossing(self, path: str) -> bool:
        curr = (0, 0)
        visited = set()
        visited.add(curr)
        for c in path:
            x, y = curr
            if c == "N":
                curr = (x, y + 1)
            elif c == "S":
                curr = (x, y - 1)
            elif c == "E":
                curr = (x + 1, y)
            elif c == "W":
                curr = (x - 1, y)

            if curr in visited:
                return True

            visited.add(curr)
            
        return False
        
