# time: O(n)
# space: O(1)
class Solution:
    def countHomogenous(self, s: str) -> int:
        cnt = 0
        i, j = 0, 0
        while i < len(s):
            while j < len(s):
                if s[i] == s[j]:
                    cnt += (j - i) + 1
                    j += 1
                else:
                    break
            i = j
                
        return cnt % (10 ** 9 + 7)

# cnt len(homo sub)
# 1   1
# 2   12 -> e.g. 'aa': 1 'a' + 1 'aa'
# 3   123
# 4   1234
# 5   12345
