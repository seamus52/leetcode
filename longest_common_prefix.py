# time: O(n^2)
# space: O(1)-ish
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        lcp = ""
        if strs == []:
            return lcp

        strs.sort(key=lambda s : len(s))

        for i in range(len(strs[0])):
            expected_char = strs[0][i]
            for s in strs:
                if s[i] != expected_char:
                    return lcp
            lcp = lcp + expected_char

        return lcp
