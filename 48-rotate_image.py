# time: O(n)
# space: O(1)
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        def transpose(m):
            for r in range(len(m)):
                for c in range(r, len(m[0])):
                    m[r][c], m[c][r] = m[c][r], m[r][c] 

        def mirror(m):
            for r in range(len(m)):
                for c in range(len(m[0]) // 2):
                    m[r][c], m[r][-c - 1] = m[r][-c - 1], m[r][c]


        transpose(matrix)
        mirror(matrix)

