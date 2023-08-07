class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        def transpose(m):
            for r in range(len(m)):
                for c in range(r, len(m[r])):
                    m[r][c], m[c][r] = m[c][r], m[r][c]

        
        def mirror(m):
            for r in range(len(m)):
                for c in range(len(m[r]) // 2):
                    m[r][c], m[r][-c - 1] = m[r][-c - 1], m[r][c]

        transpose(matrix)
        mirror(matrix)
