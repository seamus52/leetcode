# time: O(n)
# space: O(n)
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = [-1]
        max_len = 0
        for i, c in enumerate(s):
            if c == '(':
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    stack.append(i)
                else:
                    curr_len = i - stack[len(stack) - 1]
                    max_len = max(curr_len, max_len)
        return max_len
