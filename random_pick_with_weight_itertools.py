# time = O(n) init, O(log n) pick
# space = O(n) init, O(1) pick
class Solution:
    def __init__(self, w: List[int]):
        self.cumsum = list(itertools.accumulate(w))
        self.total = sum(w)

    def pickIndex(self) -> int:
        # generate a random int under the sum of weights
        rnd_num = random.randint(1, self.total)
        # find the position of that weight in the cumulative sum of weights
        # essentially, this is a storage compacted version of appending
        # each index its probability times on a list and picking from
        # that list at random
        return bisect_left(self.cumsum, rnd_num)
        

# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
