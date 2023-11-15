class Solution:
    def minDistance(self, height: int, width: int, tree: List[int], squirrel: List[int], nuts: List[List[int]]) -> int:
        def mdist(a, b):  # Manhattan distance
            return abs(a[0] - b[0]) + abs(a[1] - b[1])

        total_dist = 0
        dist = -inf
        for nut in nuts:
            total_dist += mdist(nut, tree) * 2
            dist = max(dist, mdist(nut, tree) - mdist(nut, squirrel))

        return total_dist - dist
