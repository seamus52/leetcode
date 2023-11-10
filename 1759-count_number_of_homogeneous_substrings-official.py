# time: O(n)
# space: O(1)
class Solution:
    def countHomogenous(self, s: str) -> int:
        ans = 0
        curr_streak = 0
        MOD = 10 ** 9 + 7

        for i in range(len(s)):
            if i == 0 or s[i] == s[i - 1]:
                curr_streak += 1
            else:
                curr_streak = 1
            
            ans += curr_streak
        
        return ans % MOD

# cnt len(homo sub)
# 1   1
# 2   12 -> e.g. 'aa': 1 'a' + 1 'aa'
# 3   123
# 4   1234
# 5   12345
