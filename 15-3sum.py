time: O(n^2) - sort decays into this range as O(n log n)
space: O(n) for sort
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = set()
        for i in range(len(nums) - 2):
            l = i + 1
            r = len(nums) - 1
            first = nums[i]
            while i < l < r:
                # print(i, l, r)
                second = nums[l]
                third = nums[r]
                s = first + second + third
                if s < 0:
                    l += 1
                elif s > 0:
                    r -= 1
                else:
                    res.add((first, second, third))
                    l += 1
                    r -= 1

        return res
