# backtracking part is the same as 78. Subsets
# Time: ~O(n * 2^n)
# Space: ~O(n) - only uses space for output

class Solution:
    def maxLength(self, arr: List[str]) -> int:
        def backtrack(start, combo):
            nonlocal max_len
            if start > len(arr):
                return

            combos.append(combo[:])
            s = "".join(combo) 
            if len(s) == len(set(s)):
                max_len = max(len(s), max_len)

            for i in range(start, len(arr)):
                combo.append(arr[i])
                backtrack(i + 1, combo)
                combo.pop()

        max_len = 0
        combos = []
        backtrack(0, [])

        return max_len
       
