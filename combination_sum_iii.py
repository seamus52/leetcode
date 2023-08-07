# time: factorial
# space: O(k), keep track of current combo + recursive stack, does not account for collecting the result list
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        def backtrack(start, combo):
            if len(combo) == k and sum(combo) == n:
                combos.append(combo[:])
            elif len(combo) > k or sum(combo) > n:
                return

            for num in range(start, 10):
                combo.append(num)
                backtrack(num + 1, combo)
                combo.pop()

        combos = []
        backtrack(1, [])
        return combos
