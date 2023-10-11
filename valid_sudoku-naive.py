# time: O(1) - board is always of the same size
# space: O(1)

# time: O(1) - board is always of the same size
# space: O(1)

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Each row must contain the digits 1-9 without repetition.
        for row in board:
            if not self.validate_logic(row):
                    return False

        # Each column must contain the digits 1-9 without repetition.
        for i in range(0, len(board[0])):
            column = [row[i] for row in board]
            if not self.validate_logic(column):
                    return False

        # Each of the 9 3x3 boxes must contain the digits 1-9 without repetition.
        for row_scaler in (0, 3, 6):
            for col_scaler in (0, 3, 6):
                items = []
                for row in range(3):
                    for col in range(3):
                        v = board[row + row_scaler][col + col_scaler]
                        items.append(v)

                if not self.validate_logic(items):
                    return False

        return True


    def validate_logic(self, items_to_validate):
        chars_of_items = Counter(items_to_validate)
        for k, v in chars_of_items.items():
            if k != "." and v > 1:
                return False
        
        return True

