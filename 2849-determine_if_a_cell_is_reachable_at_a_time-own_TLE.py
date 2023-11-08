class Solution:
    def isReachableAtTime(self, sx: int, sy: int, fx: int, fy: int, t: int) -> bool:
        def next(x, y):
            nx, ny = x, y
            if nx < fx: nx += 1
            if ny < fy: ny += 1
            if nx > fx: nx -= 1
            if ny > fy: ny -= 1
            return (nx, ny)

        def dist():
            x, y = sx, sy 
            d = 0
            while (x, y) != (fx, fy):
                x, y = next(x, y)
                d += 1
            return d

        if (sx, sy) == (fx, fy):
            return False

        if dist() <= t:
            return True

        return False

