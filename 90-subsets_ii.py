class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        def backtrack(i, combo):
            if len(combo) > len(nums):
                return

            combos.append(combo[:])

            for j in range(i, len(nums)):
                combo.append(j)
                backtrack(j + 1, combo)
                combo.pop()


        nums.sort()
        combos = []
        backtrack(0, [])
        res = []
        for combo in combos:
            c = [nums[j] for j in combo]
            if c not in res:
                res.append(c[:])

        return res
        
