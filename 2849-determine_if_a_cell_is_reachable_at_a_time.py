# time: O(1)
# space: O(1)
# trick: find distance between start and finish
# distance cannot be more th
class Solution:
    def isReachableAtTime(self, sx: int, sy: int, fx: int, fy: int, t: int) -> bool:
        # edge case: cannot move to self in 1 step
        if (sx, sy) == (fx, fy) and t == 1:
            return False

        # distance on grid is Chebishev distance: max of abs(diff) of coordinates
        w = abs(sx - fx)
        h = abs(sy - fy)
        c_dist = max(w, h)

        return c_dist <= t
