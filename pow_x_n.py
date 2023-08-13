#time: O(log n)
#space: O(log n)

class Solution:
    def myPow(self, x: float, n: int) -> float:
        def pow(base, exp):
            if exp == 0:
                return 1
            elif exp == -1:
                return 1 / base

            res = pow(base, exp // 2)
            if (exp % 2) == 0:
                return res * res
            else: # != 0: cannot compose with power of 2 only
                return res * res * base

        return pow(x, n)
