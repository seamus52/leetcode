# time O(n log n) - sort dominates
# space O(n) to store the sorted array
from math import sqrt
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # also works w/o sqrt:
        # points.sort(key=lambda x : x[0] ** 2 + x[1] ** 2)
        points.sort(key=lambda x : sqrt(x[0]* x[0] + x[1] * x[1]))

        return points[:k]

# study python built-in heap operations
# class Solution:
#     def kClosest(self, P, k):
#         squared_distance = lambda x, y : x*x + y*y
#         for p in P:
#             p.insert(0, squared_distance(p[0], p[1]))
#         heapify(P)
#         return [heappop(P)[1:] for i in range(k)]
