from collections import Counter
class Solution:
    def minDeletions(self, s: str) -> int:
        c = Counter(s)
        cnt = 0
        used_freq = set()

        for c, freq in c.items():
            while freq > 0 and freq in used_freq:
                freq -= 1
                cnt += 1
            used_freq.add(freq)

        return cnt
        
