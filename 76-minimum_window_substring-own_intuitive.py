# time: O(n + m)
# space: O(1)
from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        s_cnt = Counter()
        t_cnt = Counter(t)

        if t_cnt & Counter(s) != t_cnt: # s doesn't contain all the necessary chars
            return ""

        l = 0
        r = l

        min_substring = s
        
        while r < len(s):
            # expand window until a substring is found
            while s_cnt & t_cnt != t_cnt and r < len(s):
                s_cnt[s[r]] += 1
                r += 1

            # contract window to find minimum viable substring
            while s_cnt & t_cnt == t_cnt:
                s_cnt[s[l]] -= 1
                l += 1

            if len(s[l - 1:r]) < len(min_substring):
                min_substring = s[l - 1:r]

        return min_substring

