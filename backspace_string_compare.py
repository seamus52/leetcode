# use 2 stacks, push, unless backspace, compare
# time: O(n)
# space: O(n)
# can solve w/ O(1) space w/ 2 pointers:
# iterate backwards,
# check if chars at pos are equal,
# do not perform check _after_ seeing backspace
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s_s = []
        s_t = []

        for c in s:
            if c != "#":
                s_s.append(c)
            elif len(s_s) > 0:
                s_s.pop()

        for c in t:
            if c != "#":
                s_t.append(c)
            elif len(s_t) > 0:
                s_t.pop()
        
        return s_s == s_t
