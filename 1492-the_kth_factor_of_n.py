from math import sqrt
class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        factors = []
        for f in range(1, n + 1):
            if n % f == 0:
                factors.append(f)
                if len(factors) == k:
                    return factors[-1]

        return -1

