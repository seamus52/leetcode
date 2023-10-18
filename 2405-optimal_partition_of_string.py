class Solution:
    def partitionString(self, s: str) -> int:
        cnt = 1
        chars = set()
        for c in s:
            if c in chars:
                cnt += 1
                chars = set()
            chars.add(c)

        return cnt
