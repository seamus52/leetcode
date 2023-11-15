# time: O(n)
# space: O(1)
from collections import Counter
class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        cnt = 0
        c = Counter(s)
        print(c)
        for k, v in c.items():
            if v >= 2:
                l = s.index(k)
                r = s.rindex(k)
                # print(s[l+1:r])
                num_combos = set(s[l+1:r])
                cnt += len(num_combos)

        return cnt
