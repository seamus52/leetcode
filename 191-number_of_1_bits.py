# time: O(n)
# space: O(1)
class Solution:
    def hammingWeight(self, n: int) -> int:
        # return bin(n).count("1")

        cnt = 0
        while n:
            if n & 1:
                cnt += 1
            n = n >> 1
        return cnt
