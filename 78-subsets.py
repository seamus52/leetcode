# create combinations of length 1 - len(nums)
# Time: ~O(n * 2^n)
# Space: ~O(n) - only uses space for output
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def backtrack(start, combo):
            if len(combo) > len(nums):
                return

            combos.append(combo[:])

            for i in range(start, len(nums)):
                combo.append(nums[i])
                backtrack(i + 1, combo)
                combo.pop()

        combos = []
        backtrack(0, [])
        return combos
