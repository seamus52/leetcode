# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

# solution: binary search
# time: O(log n)
# space: O(1)
class Solution:
    def firstBadVersion(self, n: int) -> int:
        start = 1
        end = n

        while start < end:
            mid = (start + end) // 2
            if isBadVersion(mid):
                end = mid
            else:
                start = mid + 1 # we know mid is not bad

        return start
