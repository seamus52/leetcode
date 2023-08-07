# time: O(n log n)
# space: O(1)
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums.sort()
        
        for i in range(1, len(nums), 2):
            if nums[i - 1] != nums[i]:
                return nums[i - 1]

        # edge case: loop ends before checking last element (which at that point is unpaired)
        return nums[-1]
