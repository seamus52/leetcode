# time: O(n)
# space: O(1)
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        # Find the first non-increasing element starting from the end
        i = j = len(nums) - 1
        while i > 0 and nums[i - 1] >= nums[i]:
            i -= 1

        # There are 2 cases:
        # 1) i == 0: the array is sorted decreasingly.
        # This means that the next permutation is the first (if ordered)
        # Reverse the sequence and return.
        if i == 0:
            nums.reverse()
            return

        # 2) i != 0
        # Find the first number > nums[i - 1], starting from the end
        while nums[j] <= nums[i - 1]:
            j -= 1

        # i and j are pointing to:
        # i: first non-ascending number from end
        # j: first number greater than nums[i - 1]
        # swap these two numbers
        nums[i-1], nums[j] = nums[j], nums[i-1]
        
        # reverse the sequence strating from i to end
        nums[i:] = nums[len(nums) - 1:i - 1:-1]

