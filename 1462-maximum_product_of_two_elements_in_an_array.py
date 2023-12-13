# time: O(n)
# space: O(1)
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        prev_max = 0
        curr_max = 0
        for n in nums:
            if n > curr_max:
                prev_max = curr_max
                curr_max = n
            elif n > prev_max:
                prev_max = n

        return (prev_max - 1) * (curr_max - 1)

