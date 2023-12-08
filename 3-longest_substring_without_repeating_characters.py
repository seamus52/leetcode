# time: O(n)
# space: O(k) - size of set, upper bound size of alphabet ~ O(1)
from collections import Counter
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        c = Counter()
        l = r = 0

        max_len = 0
        while r < len(s):
            c[s[r]] += 1

            while c[s[r]] > 1:
                c[s[l]] -= 1
                l += 1

            max_len = max(max_len, r - l + 1)
            r += 1

        return max_len

