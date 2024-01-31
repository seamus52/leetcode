class Solution:
    def numSteps(self, s: str) -> int:
        n = int(s, 2)
        cnt = 0

        # print(n)
        while n != 1:
            if n % 2 == 0:
                n = n // 2
            else:
                n += 1
            cnt += 1

        return cnt
        
