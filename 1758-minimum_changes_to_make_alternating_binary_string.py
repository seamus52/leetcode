# time: O(n)
# space: O(1)
class Solution:
    def minOperations(self, s: str) -> int:
        acc = 0
        pattern = ["0", "1"]
        zero_based = 0
        for i, c in enumerate(s):
            if pattern[i % 2] != s[i]:
                zero_based += 1

        pattern = ["1", "0"]
        one_based = 0
        for i, c in enumerate(s):
            if pattern[i % 2] != s[i]:
                one_based += 1

        return min(zero_based, one_based)

