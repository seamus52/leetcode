# task re-stated:
# find longest prefix of t that is a subsequnece of s
# return len(t) - prefix length
# time: O(n)
# space: O(1)
class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        i = 0

        for c in s:
            # loop until end of t
            # check if any sequence of characters of s
            # appear in t in successive order
            if i < len(t) and t[i] == c:
                i += 1

        return len(t) - i
