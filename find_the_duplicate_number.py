# time: O(n)
# space: O(n)

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # this solution is elegant and fast, but only handles 1 duplication
        # the problem wording should allow this to work, but the test cases don't

        # expected_sum = sum(range(1, len(nums)))
        # actual_sum = sum(nums)
        # return actual_sum - expected_sum

        # this solution is not constant space :(
        # freq = Counter(nums)
        # for n in nums:
        #     if freq[n] > 1:
        #         return n

        # this solution fits the constraints but produces TLE
        # for n in nums:
        #     cnt = 0
        #     for i in range(len(nums)):
        #         if nums[i] == n:
        #             cnt += 1
        #         if cnt > 1:
        #             return n

        # (one) official solution:
        # this should not work, because it mutates the array
        # because it works, sort-based solutions should also be enabled
        # while nums[0] != nums[nums[0]]:
        #     nums[nums[0]], nums[0] = nums[0], nums[nums[0]]
        # return nums[0]

        # official solution w/ index binary search, satisfies all criteria:
        # 'low' and 'high' represent the range of values of the target
        low = 1
        high = len(nums) - 1
        
        while low <= high:
            cur = (low + high) // 2
            count = 0

            # Count how many numbers are less than or equal to 'cur'
            count = sum(num <= cur for num in nums)
            if count > cur:
                duplicate = cur
                high = cur - 1
            else:
                low = cur + 1
                
        return duplicate

        
