class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        def row(i):
            if i == 0:
                return [1]
            elif i == 1:
                return [1, 1]

            prev = row(i - 1)
            print(prev)
            return [1] + [prev[j - 1] + prev[j] for j in range(1, len(prev))] + [1]

        return row(rowIndex)
