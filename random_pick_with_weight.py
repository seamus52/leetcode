# constr time: O(n)
# constr space: O(n)
# pick time: O(n)
# pick space: O(1)

from random import randint
class Solution:

    def __init__(self, w: List[int]):
        self.cum_sums = []
        cum_sum = 0
        for weight in w:
            cum_sum += weight
            self.cum_sums.append(cum_sum)
        self.total_sum = cum_sum

    def pickIndex(self) -> int:
        target = self.total_sum * random.random()
        # run a linear search to find the target zone
        for i, cum_sum in enumerate(self.cum_sums):
            if target < cum_sum:
                return i
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
