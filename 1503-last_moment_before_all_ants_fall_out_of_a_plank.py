# max of last 2 to reach opposite edge
class Solution:
    def getLastMoment(self, n: int, left: List[int], right: List[int]) -> int:
        l = max(left) if left else 0
        r = n - min(right) if right else 0

        return max(l, r)
