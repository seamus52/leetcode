class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        def transpose(m):
            # 1-liner:
            return zip(*m)
            # clone_mat = []
            # for _ in range(len(m[0])):
            #     clone_mat.append([0] * len(m))

            # for c in range(len(m[0])):
            #     for r in range(len(m)):
            #        clone_mat[c][r] = m[r][c] 

            # return clone_mat

        return transpose(matrix)

