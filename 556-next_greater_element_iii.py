from itertools import permutations
class Solution:
    def nextGreaterElement(self, n: int) -> int:
        digits = list(str(n))
        min_candidate = inf
        
        for p in permutations(digits):
            candidate = int("".join(p))
            if candidate > n and candidate < min_candidate and candidate < 2 ** 31:
                min_candidate = candidate

        return min_candidate if min_candidate != inf else -1
        
