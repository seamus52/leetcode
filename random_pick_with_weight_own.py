# create list of w * repeated i
# constr time: O(n) - assuming avg 1 <= w[i] <= 10^5
# constr space: O(n) -> MLE
# pick time: O(1)
# pick space: O(1)

from random import randint
class Solution:

    def __init__(self, w: List[int]):
        self.w_flat = []
        for i, n in enumerate(w):
            for times in range(n):
                self.w_flat.append(i)
        

    def pickIndex(self) -> int:
        pos = randint(0, len(self.w_flat) - 1)
        return self.w_flat[pos]
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
