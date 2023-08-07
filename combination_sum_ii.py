# time: O(2^N) - worst case: all numbers unique, each number either included or not
# space: O(n)
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack(start, remain, combo):
            if remain == 0:
                combos.append(combo[:])
                return
            elif remain < 0:
                return

            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                combo.append(candidates[i])
                backtrack(i + 1, remain - candidates[i], combo)
                combo.pop()


        candidates.sort()
        combos = []
        backtrack(0, target, [])
        return combos
