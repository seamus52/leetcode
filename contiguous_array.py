# equal # of 0 and 1 -> sum of subarray == len(subarray) / 2
# result needs to be even
# plan scenario: what if we start from both ends?

#time: O(n^2)
#space: O(1)
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        prefix_sum = {0: -1}  # sum -> i
        max_len = 0
        total = 0

        for i, n in enumerate(nums):
            if n == 0:
                total -= 1
            if n == 1:
                total += 1
            if total not in prefix_sum:
                prefix_sum[total] = i
            else:
                max_len = max(max_len, i - prefix_sum[total])

        return max_len
