from collections import Counter
class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        cnt = Counter()
        for word in words:
            for c in word:
                cnt[c] += 1

        for v in cnt.values():
            if v % len(words) != 0:
                return False

        return True

