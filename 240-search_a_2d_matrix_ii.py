from bisect import bisect_left
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def col_of(matrix, i):
            return [row[i] for row in matrix]

        r_max = len(matrix)
        c_max = len(matrix[0])
        i = 0

        while i < max(r_max, c_max):
            if i < r_max:
                r_pos = bisect_left(matrix[i], target)
                # be mindful of col/row pivot in this logic
                if r_pos < c_max and matrix[i][r_pos] == target:
                    return True

            if i < c_max:
                c_pos = bisect_left(col_of(matrix, i), target)
                # be mindful of col/row pivot in this logic
                if c_pos < r_max and matrix[c_pos][i] == target:
                    return True

            i += 1

        return False
