# time: O(2^n)
# space: O(2^n) - recursive stack
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def dfs(opening, closing, s):
            nonlocal combos
            # base case
            # append to results if the size is right
            # rest of the code guarantees well-formed string
            if len(s) == n * 2:
                combos.append(s)
                return 

            # add opening parenthese to string up until we reach n (0-indexed)
            if opening < n:
                dfs(opening + 1, closing, s + "(")

            # add closing parenthese to string up until we reach n (0-indexed)
            if closing < opening:
                dfs(opening, closing + 1, s + ")")

        combos = []
        dfs(0, 0, "")

        return combos
