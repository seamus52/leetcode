class Solution:
    def numberOfSteps(self, num: int) -> int:
        n = num
        cnt = 0
        while n != 0:
            if n % 2 == 0:
                n //= 2
            else:
                n -= 1
            cnt += 1

        return cnt
