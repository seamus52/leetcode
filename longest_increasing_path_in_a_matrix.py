# naive: simple path collection from each node, neighbors() to exclude ineligible path
# optimized: merge with longest path in memo for each node

# time: O(m*n) - due to memo, each cell is calculated once only
# space: O(m*n) worst case - recursive calls
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        def in_bounds(matrix, r, c):
            return 0 <= r < len(matrix) and 0 <= c < len(matrix[0])

        
        def neighbors(matrix, r, c):
            neighbors = []
            if in_bounds(matrix, r + 1, c):
                if matrix[r][c] < matrix[r + 1][c]:
                    neighbors.append((r + 1, c))
            if in_bounds(matrix, r - 1, c):
                if matrix[r][c] < matrix[r - 1][c]:
                    neighbors.append((r - 1, c))
            if in_bounds(matrix, r, c + 1):
                if matrix[r][c] < matrix[r][c + 1]:
                    neighbors.append((r, c + 1))
            if in_bounds(matrix, r, c - 1):
                if matrix[r][c] < matrix[r][c - 1]:
                    neighbors.append((r, c - 1))
            return neighbors


        def find_path(matrix, r, c, memo):
            nonlocal max_path

            if (r, c) in memo:
                return memo[(r, c)]                

            path = 1
            for (nr, nc) in neighbors(matrix, r, c):
                path = max(path, 1 + find_path(matrix, nr, nc, memo))
            
            memo[(r, c)] = path
            return path


        max_path = 0
        memo = {}
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                max_path = max(max_path, find_path(matrix, r, c, memo))

        return max_path
