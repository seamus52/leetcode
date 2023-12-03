# time: O(n)
# space: O(1)
# chebishev distance
class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        t = 0
        prev_x, prev_y = points[0]
        for x, y in points[1:]:
            t += max(abs(x - prev_x), abs(y - prev_y))
            prev_x, prev_y = x, y

        return t

