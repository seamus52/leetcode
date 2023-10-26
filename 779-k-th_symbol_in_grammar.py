class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        def flip(d):
            return 1 if d == 0 else 0

        def recurse(n, k):
            if n == 1:
                return 0

            prev_mid = 2 ** (n - 2)

            if k <= prev_mid:
                return recurse(n - 1, k)
            else:
                return flip(recurse(n - 1, k - mprev_mid))

        return recurse(n, k)
