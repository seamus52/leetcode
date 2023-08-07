# time: O(n)
# space: O(1) - counter dict takes minimal extra space
from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        letters = Counter(magazine)
        for c in ransomNote:
            if c in letters:
                n = letters[c]
                n -= 1
                letters[c] = n
                if n < 0:
                    return False
                if n == 0:
                    del letters[c]
            else:
                return False

        return True

