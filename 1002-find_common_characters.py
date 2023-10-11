from collections import Counter
class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        if not words:
            return []
        
        d = {}  # word -> Counter(word)
        for word in words:
            d[word] = Counter(word)
            
        common = Counter(words[0])
        for v in d.values():
            common = common & v
            
        res = []
        for k, v in common.items():
            for i in range(v):
                res.append(k)
                   
        return res
