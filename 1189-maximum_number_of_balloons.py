from collections import Counter
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        c_text = Counter(text)
        c_balloon = Counter("balloon")

        cnt = 0
        while c_text & c_balloon == c_balloon:
            cnt += 1
            c_text -= c_balloon

        return cnt

