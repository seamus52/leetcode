from bisect import bisect_left
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for _, row in enumerate(matrix):
            if row[0] <= target and target <= row[-1]:
                insert_point = bisect_left(row, target)
                # print(row, insert_point, matrix[insert_point], target)
                return row[insert_point] == target

        return False
