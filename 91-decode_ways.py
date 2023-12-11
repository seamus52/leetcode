# time: O(n)
# space: O(n) - memo & recursive stack
class Solution:
    def numDecodings(self, s: str) -> int:
        @lru_cache(maxsize=None)
        def recurse_dp(start, s):
            # Reached end of the string: return 1 for success.
            if start == len(s):
                return 1

            # If the string starts with a zero, it can't be decoded
            if s[start] == "0":
                return 0

            # Reaching last character: return 1 for success.
            # May seem out of order and illogical at first, but this sequencing
            # is needed for the recursive +1 vs +2 logic to terminate correctly
            if start == len(s) - 1:
                return 1

            cnt = recurse_dp(start + 1, s)
            if int(s[start:start + 2]) <= 26:
                cnt += recurse_dp(start + 2, s)

            return cnt


        return recurse_dp(0, s)
