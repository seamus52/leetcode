# create dict of char frequency
# longest palindrome = # of 2n frequencies + 1, if any such freq exists
# time: O(n)
# space: O(1)
class Solution:
    def longestPalindrome(self, s: str) -> int:
        freq = Counter(s)
        # print(freq)

        palindrome_length = 0
        odd_picked = False
        for v in freq.values():
            palindrome_length += (v // 2) * 2
            if v % 2 != 0 and not odd_picked:
                palindrome_length += 1
                odd_picked = True

        return palindrome_length
