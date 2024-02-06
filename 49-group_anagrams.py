from collections import Counter, defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)

        for s in strs:
            d[frozenset(Counter(s).items())].append(s)

        return [v for v in d.values()]
        
