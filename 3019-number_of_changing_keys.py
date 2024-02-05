class Solution:
    def countKeyChanges(self, s: str) -> int:
        cnt = 0
        prev = s[0]
        
        for c in s:
            if prev.lower() != c.lower():
                cnt += 1
            prev = c

        return cnt
    
