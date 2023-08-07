# use stack
# Time complexity : O(n) because we simply traverse the given string one character at a time and push and pop operations on a stack take O(1)O(1)O(1) time.
# Space complexity : O(n) as we push all opening brackets onto the stack and in the worst case, we will end up pushing all the brackets onto the stack. e.g. ((((((((((.
class Solution:
    def isValid(self, s: str) -> bool:
        opening = "([{"
        closing = ")]}"
        stack = []

        for c in s:
            if c in opening:
                stack.append(c)
            
            if len(stack) == 0:
                return False

            if c in closing:
               pair = stack.pop()
               if opening.index(pair) != closing.index(c):
                   return False

        if len(stack) != 0:
            return False

        return True
