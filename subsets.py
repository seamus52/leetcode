# create combinations of length 1 - len(nums)
# Time: ~O(n * n choose k)
# Space: ~O(n * n choose k)
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets = []
        for i in range(len(nums) + 1):
            for combo in self.create_combinations(nums, i):
                subsets.append(combo)
        return subsets


    def create_combinations(self, items, k):
        if len(items) < k:
            return []

        if k == 0:
            return [[]]

        first = items[0]
        combos_with_first = []
        for combo in self.create_combinations(items[1:], k - 1):
            combos_with_first.append([first, *combo])

        combos_without_first = self.create_combinations(items[1:], k)

        return combos_with_first + combos_without_first
