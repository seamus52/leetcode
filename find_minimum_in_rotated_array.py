# time: O(log n)
# space: O(1)
class Solution:
    def findMin(self, nums: List[int]) -> int:
        # edge case: list has one element
        if len(nums) == 1:
            return nums[0]

        left = 0
        right = len(nums) - 1

        # edge case: array is already sorted
        if nums[right] > nums[0]:
            return nums[0]

        while right >= left:
            mid = (left + right) // 2
            # if the mid value > its next element then mid + 1 element is min
            if nums[mid] > nums[mid + 1]:
                return nums[mid + 1]
            # if the mid value < its previous element then mid element is min
            if nums[mid - 1] > nums[mid]:
                return nums[mid]

            # if the mid value > than the 0th element, min is to the right
            if nums[mid] > nums[0]:
                left = mid + 1
            # if nums[0] is > than the mid value, min is to the left
            else:
                right = mid - 1
