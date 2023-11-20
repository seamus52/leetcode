# time: O(n)
# space: O(1)
class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        travel = [0] + travel
        acc = 0
        m = {}
        g = {}
        p = {}
        for i, house in enumerate(garbage):
            l = list(house)
            if "M" in l:
                m[i] = l.count("M")
            if "G" in l:
                g[i] = l.count("G")
            if "P" in l:
                p[i] = l.count("P")

        if m:
            acc += sum(travel[:max(m.keys()) + 1])
        for i, units in m.items():
            acc += units

        if g:
            acc += sum(travel[:max(g.keys()) + 1])
        for i, units in g.items():
            acc += units

        if p:
            acc += sum(travel[:max(p.keys()) + 1])
        for i, units in p.items():
            acc += units
        
        return acc

