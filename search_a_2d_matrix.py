# time: O(m * n)
# space: O(n)
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # official solution
        # if not matrix or len(matrix) == 0: return False
        # r = len(matrix)
        # c = len(matrix[0])
        
        # # treat the matrix as a virtual array and do binary search
        # left, right = 0, r * c - 1
        # while left <= right:
        #         mid = (left + right) // 2
        #         mid_element = matrix[mid // c][mid % c]
        #         if target == mid_element:
        #             return True
        #         else:
        #             if target < mid_element:
        #                 right = mid - 1
        #             else:
        #                 left = mid + 1
        # return False

        # concise solution using bisect
        # row_idx = bisect_left(matrix, target, key=lambda row : row[-1])
        # return row_idx < len(matrix) and matrix[row_idx][bisect_left(matrix[row_idx], target)] == target

        # locate row
        last_of_rows = [line[-1] for line in matrix]
        row_idx = bisect_left(last_of_rows, target)
        print(row_idx)

        # locate item
        if row_idx < len(matrix):
            if matrix[row_idx][bisect_left(matrix[row_idx], target)] == target:
                return True

        return False
