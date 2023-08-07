# time: O(n^2)
# space: O(n) - length of DP array
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        def max_increasing_subseq(nums, i, prev, memo):
            if (i, prev) in memo:
                return memo[(i, prev)]
            
            if i == len(nums):
                return 0
            
            curr = nums[i]
            include = 0
            if prev < curr:
                include = 1 + max_increasing_subseq(nums, i + 1, curr, memo)
            
            exclude = max_increasing_subseq(nums, i + 1, prev, memo)
            
            memo[(i, prev)] = max(include, exclude)
            return max(include, exclude)
        
        memo = {}
        return max_increasing_subseq(nums, 0, float("-inf"), memo)
