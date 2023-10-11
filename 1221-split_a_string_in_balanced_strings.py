class Solution:
    def balancedStringSplit(self, s: str) -> int:
        d = {"R": 0, "L": 0}
        cnt = 0
        
        for c in s:
            d[c] += 1
            
            if d["L"] == d["R"]:
                cnt += 1
                d = {"R": 0, "L": 0}
        
        return cnt
