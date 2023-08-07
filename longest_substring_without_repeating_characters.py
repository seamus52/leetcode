# time: O(char*max_len) -> behaves like < O(n^2)
# space: O(n) - set space is negligible
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        longest  = 0
        for i in range(len(s)):
            chars_seen = set()
            length = 0
            for j in range(i, len(s)):
                if s[j] in chars_seen:
                    break
                else:
                    chars_seen.add(s[j])
                    length += 1
                    if length > longest:
                        longest = length

        return longest
