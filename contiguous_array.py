# equal # of 0 and 1 -> sum of subarray == len(subarray) / 2
# result needs to be even
# plan scenario: what if we start from both ends?

#time: O(n^2)
#space: O(1)
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        max_length = 0
        interval_sum = 0

        for i in range(len(nums)):
            interval_sum +=  nums[i]
            delta_sum = 0
            for j in range(i + 1, len(nums)):
                # print(nums[i:j + 1])
                interval_sum += nums[j]
                delta_sum += nums[j]
                if interval_sum == len(nums[i:j + 1]) / 2:
                    max_length = max(len(nums[i:j + 1]), max_length)
            interval_sum -= delta_sum
            interval_sum -=  nums[i]

        return max_length

