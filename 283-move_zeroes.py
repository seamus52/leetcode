# time: O(n)
# space: O(1)

# 2 pointers
# Use one pointer at index(start) = 0
# and use a loop to traverse through the array and move non zero element to index (start)
class Solution:
    def moveZeroes(self, nums):
        i = 0
        for j in range(len(nums)):
            if (nums[j] != 0):
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
