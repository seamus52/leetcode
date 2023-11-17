# time: O(n log n)
# space: O(n)
class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        max_psum = 0
        nums.sort()
        l = 0
        r = len(nums) - 1
        while l < r:
            max_psum = max(max_psum, nums[l] + nums[r])
            l += 1
            r -= 1

        return max_psum
