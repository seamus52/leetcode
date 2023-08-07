# sliding window: char freq count of s, maintain
# match against char freq count of p
# time: O(n)
# space: O(n)

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        anagrams = []
        p_chars = Counter(p)
        window_chars = Counter(s[0:len(p)])
        if window_chars == p_chars:
            anagrams.append(0)

        for i in range(1, len(s) - len(p) + 1):
            # slide left bound of window
            window_chars[s[i - 1]] -= 1
            if window_chars[s[i - 1]] < 1:
                del window_chars[s[i - 1]]

            # slide right bound of window
            window_chars[s[i + len(p) - 1]] += 1

            if window_chars == p_chars:
                anagrams.append(i)

        return anagrams
