# stack - handle nesting -> put back to stack
# time: O(approx k^k*n)
# space: O(approx k^k*n)

class Solution:
    def decodeString(self, s: str) -> str:
        curr_string = ""
        curr_num = 0
        stack = []

        for c in s:
            if c == "[":
                stack.append(curr_string)
                stack.append(curr_num)
                curr_string = ""
                curr_num = 0
            elif c == "]":
                num = stack.pop()
                prev_string = stack.pop()
                curr_string = prev_string + num * curr_string
            elif c.isdigit():
                curr_num = curr_num * 10 + int(c)
            else:
                curr_string += c

        return curr_string
