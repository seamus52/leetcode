# time: O(m * n)
# space: O(m + n)
class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        counts_per_row = []
        for row in mat:
            counts_per_row.append(row.count(1))

        counts_per_col = []
        for c in range(len(mat[0])):
            col = []
            for r in range(len(mat)):
                col.append(mat[r][c])
            counts_per_col.append(col.count(1))

        print(counts_per_row)
        print(counts_per_col)

        cnt = 0
        for r in range(len(mat)):
            for c in range(len(mat[0])):
                if mat[r][c] == 1:
                    if counts_per_row[r] == 1 and counts_per_col[c] == 1:
                        cnt += 1

        return cnt

