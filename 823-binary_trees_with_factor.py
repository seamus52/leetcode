class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        arr.sort()

        d = {}
        for e in arr:
            d.setdefault(e, 1)
        
        for e in arr:
            for factor in arr:
                if factor == e:
                    break
                if e % factor == 0 and e // factor in d:
                    d[e] += d[factor] * d[e // factor]
        return sum(d.values()) % (pow(10, 9) + 7)

