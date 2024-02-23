class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        d = {}
        for a, b in trust:
            d.setdefault(a, set())
            d[a].add(b)

        candidates = []

        for j in range(1, n + 1):
            if j not in d:
                candidates.append(j)
        
        if not candidates or len(candidates) > 1:
            return -1

        candidate = candidates[0]
        for v in d.values():
            if candidate not in v:
                return -1

        return candidate

