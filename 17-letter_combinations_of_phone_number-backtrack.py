# time: O(4^n * m)
# space: O(1) - recursion stack is not using more than the input
from itertools import product
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        buttons = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"]
        }

        def backtrack(i, combo):
            if len(combo) == len(digits):
                combos.append("".join(combo))
                return

            possible_letters = buttons[digits[i]]
            for l in possible_letters:
                combo.append(l)
                backtrack(i + 1, combo)
                combo.pop()


        if not digits:
            return []

        combos = []
        backtrack(0, [])
        return combos

