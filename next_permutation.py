# time: O(n)
# space: O(1)

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # To find next permutations, we'll start from the end
        i = j = len(nums)-1
        # First we'll find the first non-increasing element starting from the end
        while i > 0 and nums[i - 1] >= nums[i]:
            i -= 1
        # After completion of the first loop, there will be two cases

        # 1. i == 0, meaning that array is sorted decreasingly.
        # Reverse the sequence and return.
        if i == 0:
            nums.reverse()
            return

        # 2. i != 0 -> find the first number > nums[i-1], starting from end
        while nums[j] <= nums[i-1]:
            j -= 1

        # i and j are pointing to:
        # i - first non-ascending number from end
        # j - first number greater than nums[i - 1]
        
        # these two numbers
        nums[i-1], nums[j] = nums[j], nums[i-1]
        
        # reverse the sequence strating from i to end
        nums[i:]= nums[len(nums) - 1:i - 1:-1]
        # We don't need to return anything as we've modified nums in-place
