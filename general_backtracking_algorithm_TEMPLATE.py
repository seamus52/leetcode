# solution for https://leetcode.com/problems/combination-sum/description/
# m = min value across candidates
# t = tree depth
# time: O(n^m)
# space O(t/m)
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        results = []
        def backtrack(remain, comb, start):
            if remain == 0: # base case 1: candidate completes the target sum
                results.append(comb[:])
                return
            elif remain < 0: # base case 2: target sum canot be achieved
                return

            for i in range(start, len(candidates)):
                # add the number into the combination
                comb.append(candidates[i])
                # duplication was permitted: give the current number another chance
                backtrack(remain - candidates[i], comb, i)
                # backtrack, remove the number from the combination
                comb.pop()

        backtrack(target, [], 0)
        return results
