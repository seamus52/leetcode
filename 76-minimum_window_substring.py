#time: O(s+t)
#space: O(s+t)

from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        """
        Two pointers, left and right
        Both start from 0,0
        Increase right pointer until valid window is found
        Decrease left pointer until window is no longer valid
        Add the minimum length window you've found to your results
        Continue increasing right pointer, pretty much repeating what we did above
        Return the minimum length of results
        """
        s_count, t_count = Counter(), Counter(t)
        l, r = 0, 0
        results = []

        while r <= len(s) - 1:
            # Find valid window
            s_count[s[r]] += 1
            r += 1
            # & operator on Counter = intersection: checks min count in both counters
            # intersection is required for deriving a common set
            # s_count may contain characters not in t_count, which would render the
            # comparison false
            if s_count & t_count != t_count:
                continue

            # Minimize this window
            while l < r:
                s_count[s[l]] -= 1
                l += 1
                if s_count & t_count == t_count:
                    continue
                results.append(s[l - 1:r])
                break

        return min(results, key=len) if results else ""
