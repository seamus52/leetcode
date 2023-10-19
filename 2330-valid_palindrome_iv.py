class Solution:
    def makePalindrome(self, s: str) -> bool:
        mid = len(s) // 2
        l = 0
        r = len(s) - 1
        cnt = 0

        while l <= r:
            if s[l] != s[r]:
                cnt+= 1
            # print(s[l], s[r], cnt)                
            if cnt > 2:
                break
            l += 1
            r -= 1

        return cnt <= 2
