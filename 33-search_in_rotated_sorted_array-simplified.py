# time: O(log(n))
# space: O(1)
# trick: bsearch on both sides of pivot (but make sure top include)
from bisect import bisect_left
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def find_pivot(nums):
            start = 0
            end = len(nums) - 1

            while start <= end:
                mid = (start + end) // 2
                if nums[mid] > nums[mid + 1]:
                    return mid + 1
                if nums[mid] < nums[mid - 1]:
                    return mid

                if nums[mid] > nums[0]:
                    start = mid + 1
                if nums[mid] < nums[0]:
                    end = mid - 1

        # edge cases
        if len(nums) == 1:  # array has 1 element
            return 0 if nums[0] == target else -1
        
        if nums[0] < nums[-1]:  # array is already sorted
            idx = bisect_left(nums, target)
            if idx < len(nums) and nums[idx] == target:
                return idx
            else:
                return -1

        pivot = find_pivot(nums)

        l_idx = bisect_left(nums[:pivot], target)
        if l_idx < pivot and nums[l_idx] == target:
            return l_idx

        r_idx = bisect_left(nums[pivot:], target)
        if r_idx < len(nums) - pivot and nums[pivot + r_idx] == target:
            return pivot + r_idx

        return -1

