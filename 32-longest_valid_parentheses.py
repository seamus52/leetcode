# time: O(n)
# space: O(n)
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        # stack, used to record index of parenthesis
        # initialized to -1 as dummy head for valid parentheses length computation
        stack = [-1] # for case like: "()()()", otherwise the first pair of brackets would not be detected
        max_length = 0
        
		# linear scan each index and character in input string s
        for i, c in enumerate(s):
            if c == '(':
                # push when current char is '('
                stack.append(i)
            else:
                # pop when current char is ')'
                stack.pop()
                if not stack: # stack is empty
                    # push current index into stack
                    # we know that this value will eventually be popped
                    stack.append(i)
                else:
                    # stack is non-empty, update maximal valid parentheses length
                    max_length = max(max_length, i - stack[-1])
                
        return max_length
