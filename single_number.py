# time: O(n)
# space: O(1)
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        a = 0
        for i in nums:
            # intuition:
            # XOR a bit 2x -> becomes 0
            # pairs will even out at 0 at every bit,
            # leaving the number with no pair
            a ^= i
        return a
