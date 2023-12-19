# time: O(n^2)
# space: O(1)
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        ans = set()

        for a in range(len(nums) - 3):
            for b in range(a + 1, len(nums) - 2):
                c = b + 1
                d = len(nums) - 1

                while c < d:
                    first = nums[a]
                    second = nums[b]
                    third = nums[c]
                    fourth = nums[d]

                    s = first + second + third + fourth

                    if s == target:
                        ans.add((first, second, third, fourth))
                        c += 1
                        d -= 1
                    elif s < target:
                        c += 1
                    elif s > target:
                        d -= 1

        return ans

