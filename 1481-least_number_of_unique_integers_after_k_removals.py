from collections import Counter
class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        c = Counter(arr)

        freq = sorted(list(c.values()))
        
        removed = 0
        for i in range(len(freq)):
            removed += freq[i]

            if removed > k:
                return len(freq) - i
        
        return 0
    
