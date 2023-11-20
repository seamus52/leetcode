class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        travel = travel
        acc = 0
        d = {"M": [], "G": [], "P": []}
        for i, house in enumerate(garbage):
            if "M" in house:
                d["M"].append(i)
            if "G" in house:
                d["G"].append(i)
            if "P" in house:
                d["P"].append(i)

        for type in d:
            houses = d[type]
            if houses:
                acc += sum(travel[:houses[-1]])
            for house in houses:
                acc += garbage[house].count(type)
            
        return acc

