class Solution:
# time: O(n log n) - sliding window is O(n)
# space: O(1)
class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        l = 0
        ans = 0
        curr = 0  # tracks increments distributed in sliding window
        
        for r in range(len(nums)):
            target = nums[r]  # we want to increase values up to target
            curr += target
            
            # sliding window l -> r * target 
            while (r - l + 1) * target - curr > k:
                # make window narrower to fit k distributable increments
                curr -= nums[l]
                l += 1
            
            ans = max(ans, r - l + 1) # keep track of max window stretch

        return ans

