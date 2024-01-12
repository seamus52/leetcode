# time: O(2^N) - worst case: all numbers unique, each number either included or not
# space: O(n)
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack(start, remain, combo):
            if remain == 0:
                combos.append(combo[:])
                return
            if remain < 0:
                return

            for i in range(start, len(candidates)):
                # no repeats allowed, if two numbers following each outher in candidates are athe same, they will only be used 1x, which
                # ensures that backtrack uses them to create a combo
                # according to their original frequency in input
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                combo.append(candidates[i])
                backtrack(i + 1, remain - candidates[i], combo)
                combo.pop()

        
        # ensure candidates are processed in increasing order
        candidates.sort()
        combos = []
        backtrack(0, target, [])
        return combos

