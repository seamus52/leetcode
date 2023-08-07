# time: O(n)
# space: O(1)
class NumArray:
    def __init__(self, nums: List[int]):
        self.cumsum = [0] + list(itertools.accumulate(nums))
        print(self.cumsum)
        

    def sumRange(self, left: int, right: int) -> int:
        return self.cumsum[right + 1] - self.cumsum[left]
        

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
