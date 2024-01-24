class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        j = set(jewels)
        cnt = 0
        for s in stones:
            if s in j:
                cnt += 1

        return cnt

