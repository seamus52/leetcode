class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        outgoing = set()
        for a, b in paths:
            outgoing.add(a)

        for a, b in paths:
            if b not in outgoing:
                return b

