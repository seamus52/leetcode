# DO NOT USE DEFAULT PARAMETER VALUES to initialize an array: confuses tests!
# time: O(n)
# space: O(n) - recursion stack frames
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        visited = []
        return self._floodFill(image, sr, sc, color, visited)


    def _floodFill(self, image: List[List[int]], sr: int, sc: int, color: int, visited) -> List[List[int]]:
        prev_color = image[sr][sc]
        image[sr][sc] = color
        visited.append((sr, sc))

        for nr, nc in self.neighbors(image, sr, sc):
            if (nr, nc) not in visited and self.in_bounds(image, nr, nc):
                if image[nr][nc] == prev_color:
                    self._floodFill(image, nr, nc, color, visited)

        return image

    def in_bounds(self, image, row, col):
        return 0 <= row < len(image) and 0 <= col < len(image[0])

    def neighbors(self, image, row, col):
        neighbors = []
        neighbors.append((row - 1, col))
        neighbors.append((row + 1, col))
        neighbors.append((row, col - 1))
        neighbors.append((row, col + 1))
        return neighbors
