from itertools import permutations
from collections import Counter, deque
class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        perimeter = sum(matchsticks)
        side = perimeter // 4

        if side * 4 != perimeter:
            return False

        for p in set(permutations(matchsticks)):
            sides = [0, 0, 0, 0]
            q = deque(p)
            i = 0
            while q:
                sides[i % 4] += q.popleft()
                i += 1
            if sides.count(side) == 4:
                return True

        return False

