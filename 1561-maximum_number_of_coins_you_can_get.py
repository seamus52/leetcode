# time: O(log n)
# space: O(1)
class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort(reverse=True)
        acc = 0
        l = -1
        r = len(piles) - 1
        while l < r:
            l += 2
            r -= 1
            acc += piles[l]
        return acc
        
