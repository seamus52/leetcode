# time: O(n^2)
# time: O(log n) or O(n), depending on sort implementation
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        if len(nums) == 3:
            return sum(nums)

        nums.sort()

        min_diff = float("inf")
        closest_sum = float("inf")

        for i in range(len(nums)):
            l = i + 1
            r = len(nums) - 1

            while l < r:
                s = nums[i] + nums[l] + nums[r]
                diff = abs(target - s)
                # print(nums[i], nums[l], nums[r], diff, closest_sum)

                if diff < min_diff:
                    min_diff = diff
                    closest_sum = s

                if s < target:
                    l += 1
                else:
                    r -= 1

        return closest_sum

        

