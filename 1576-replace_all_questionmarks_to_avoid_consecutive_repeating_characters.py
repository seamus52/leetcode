from random import choice
from string import ascii_lowercase
class Solution:
    def modifyString(self, s: str) -> str:
        s = "$" + s + "$"
        res = list(s)

        for i in range(1, len(res) -1):
            if res[i] == "?":
                res[i] = choice(ascii_lowercase)
                while res[i] == res[i - 1] or res[i] == res[i + 1]:
                    res[i] = choice(ascii_lowercase)

        return "".join(res)[1:-1]
        
