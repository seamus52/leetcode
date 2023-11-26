# time: O(n)
# space: O(n) - prefix sum
class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        prefix = list(accumulate(nums))
        ans = [0] * len(nums)

        for i in range(len(nums)):
            left_sum = prefix[i] - nums[i]
            right_sum = prefix[-1] - prefix[i]
            
            left_count = i
            right_count = len(nums) - 1 - i
            
            left_total = left_count * nums[i] - left_sum
            right_total = right_sum - right_count * nums[i]

            ans[i] = left_total + right_total
        
        return ans
