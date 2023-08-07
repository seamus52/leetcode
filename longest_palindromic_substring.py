#time: better than O(n^2)
#space: O(n^2) for memo
class Solution:
    def longestPalindrome(self, s: str) -> str:
        # optimization 1: memoization
        @lru_cache
        def is_palindrome(s):
            return s == s[::-1]

        max_p = ""
        for i in range (len(s)):
            # optimization 2:
            # no point testing substrings that are smaller than max
            for j in range(i + len(max_p) - 1, len(s) + 1):
                if is_palindrome(s[i:j]):
                    if len(s[i:j]) > len(max_p):
                        max_p = s[i:j]

        return max_p
