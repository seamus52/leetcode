# robFrom(i) = max(nums(i) + robFrom(i + 2), robFrom(i + 1))
# robFrom(idx_of_house_to_examine, nums)
# At each step of recursive call, either rob, or not rob.
# next house for rob scenario: robFrom(i + 2, nums). The answer here would be whatever is returned by robFrom(i + 2, nums)
# next house for not rob scenario: robFrom(i + 1, nums)
# cache overlapping parts of solution tree
# robFrom(0, nums) will give us the answer to the entire problem.

# time: O(n)
# space: O(n)

class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}
        return self.rob_from(0, nums, memo)


    def rob_from(self, i, nums, memo):
        if i >= len(nums):
            return 0

        if i in memo:
            return memo[i]

        result = max(nums[i] + self.rob_from(i + 2, nums,  memo), self.rob_from(i + 1, nums, memo))
        memo[i] = result

        return result
