# 0-indexed Fibonacci sequence
class Solution:
    def climbStairs(self, n: int) -> int:
        # recursive solution times out
        # if n < 2:
        #     return 1

        # return self.climbStairs(n - 2) + self.climbStairs(n - 1)

        # iterative solution
        # time: O(n)
        # space: O(n)
        d = {}
        d[0] = 1
        d[1] = 1
        d[2] = 2
        if n in d:
            return d[n]
        for i in range(3, n + 1):
            d[i] = d[i - 2] + d[i - 1]

        return d[n]
        
