# time: O(n)
# space: O(1)
from collections import Counter
class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        c = Counter(chars)
        good = 0
        for w in words:
            if Counter(w) | c == c:
                good += len(w)

        return good

