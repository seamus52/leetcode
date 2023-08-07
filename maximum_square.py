# loop through matrix
# find largest square from cell
# optimization: terminate when a larger square could not exist
# time: O(m*n)
# space: O(1)

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        max_square = 0
        n = len(matrix)
        m = len(matrix[0])

        for i in range(n):
            for j in range(m):
                matrix[i][j] = int(matrix[i][j])

                if i - 1 >= 0 and j-1 > = 0 and matrix[i][j] != 0:
                    matrix[i][j] + = min(matrix[i - 1][j], matrix[i][j - 1], matrix[i - 1][j - 1])
                max_square = max(max_square, matrix[i][j])
        
        return max_square ** 2
