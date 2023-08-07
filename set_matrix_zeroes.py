# time: O(n)-ish - process each cell ~3n times worst case
# space: O(n+m) - set to store affected rows/cols, more compact than a full matrix
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows = set()
        cols = set()

        # identify and store 1
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if matrix[r][c] == 0:
                    rows.add(r)
                    cols.add(c)

        # process rows
        set_row = [0 for e in matrix[0]]
        for r in rows:
            matrix[r] = set_row

        # process cols
        for r in range(len(matrix)):
            for c in cols:
                matrix[r][c] = 0
