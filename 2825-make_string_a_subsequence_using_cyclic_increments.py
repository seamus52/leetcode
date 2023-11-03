from string import ascii_lowercase
from collections import deque
class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        def next_letter(c):
            if c == "z":
                return "a"
            idx = ascii_lowercase.index(c)
            return ascii_lowercase[idx + 1]

        i = 0
        for c in str1:
            if c == str2[i] or next_letter(c) == str2[i]:
                i += 1
            if i == len(str2):
                return True
        return False

