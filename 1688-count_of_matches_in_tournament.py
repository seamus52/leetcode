# time: O(log(n))
# space: O(1)
class Solution:
    def numberOfMatches(self, n: int) -> int:
        if n < 2:
            return 0

        if n == 2:
            return 1

        s = 0
        while n > 1:
            if n % 2 == 0:
                n = n // 2
                s += n
            else:
                n = (n - 1) // 2 + 1
                s += n - 1

        return s
