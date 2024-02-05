from collections import Counter
class Solution:
    def firstUniqChar(self, s: str) -> int:
        d = {}

        for c in s:
            d.setdefault(c, 0)
            d[c] += 1

        first_uniq_char = None
        for k, v in d.items():
            if v == 1:
                first_uniq_char = k
                break

        if first_uniq_char:
            return s.index(first_uniq_char)

        return -1

