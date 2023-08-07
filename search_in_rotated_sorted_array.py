# 1) find rotation point (using a form of binary search)
# 2) determine which section is to be searched for value
# 3) binary search for value
# time: O(log n)
# space: O(1)

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def find_pivot(nums):
            start = 0
            end = len(nums) - 1

            while end >= start:
                mid = (start + end) // 2
                # if the mid value > its next element then mid + 1 element is min
                if nums[mid] > nums[mid + 1]:
                    # return nums[mid + 1]
                    return mid + 1
                # if the mid value < its previous element then mid element is min
                if nums[mid - 1] > nums[mid]:
                    # return nums[mid]
                    return mid

                # if the mid value > than the 0th element, min is to the right
                if nums[mid] > nums[0]:
                    start = mid + 1
                # if nums[0] is > than the mid value, min is to the left
                else:
                    end = mid - 1


        def bsearch(nums, target):
            start = 0
            end = len(nums) - 1

            while start <= end:
                mid = (start + end) // 2
                if nums[mid] == target:
                    return mid
                elif nums[mid] < target:
                    start = mid + 1
                elif nums[mid] > target:
                    end = mid - 1

            return -1


        if not nums:
            return -1

        if len(nums) == 1:
            return 0 if nums[0] == target else - 1

        if nums[0] < nums[-1]: # array is sorted
            return bsearch(nums, target)

        pivot = find_pivot(nums)
        print(pivot)

        start = 0
        end = len(nums) - 1
        if target == nums[end]:
            return end
        elif target < nums[end]:
            i = bsearch(nums[pivot:], target)
            return pivot + i if i > -1 else -1
        elif target > nums[end]:
            print(nums[pivot + 1:])
            return bsearch(nums[:pivot + 1], target)

