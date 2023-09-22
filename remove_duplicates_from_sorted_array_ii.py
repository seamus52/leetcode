class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # go through the numbers and include those in the result that
        # haven't been included twice already
        i = 0
        for n in nums:
            if i < 2 or n > nums[i - 2]:
                nums[i] = n
                i += 1
        
        return i
