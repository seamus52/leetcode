# time: O(n^2)
# space: O(1)
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        cnt = 0
        for i in range(len(nums)):
            substr_sum = nums[i]
            for j in range(i, len(nums)):
                if i != j:
                    substr_sum += nums[j]
                if substr_sum == k:
                    cnt += 1

        return cnt
