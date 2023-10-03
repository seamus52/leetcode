# time: O(n choose k)
# space: O(k)
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def backtrack(start, combo):
            if len(combo) == k:
                combos.append(combo[:])
                return

            for x in range(start, n + 1):
                if x not in combo:
                    combo.append(x)
                    backtrack(x + 1, combo)
                    combo.pop()


        combos = []
        backtrack(1, [])
        return combos
