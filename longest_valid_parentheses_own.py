# time: O(n^3)
# space: O(n)
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        def is_valid(p):
            s = []
            for c in p:
                if c == "(":
                    s.append(c)
                else:
                    if s:
                        if s.pop() != "(":
                            return False
                    else:
                        return False

            if s:
                return False

            return True

        max_valid = 0
        for i in range(len(s)):
            for j in range(i + 1, len(s) + 1):
                if is_valid(s[i:j]):
                    max_valid = max(j - i, max_valid)

        return max_valid


