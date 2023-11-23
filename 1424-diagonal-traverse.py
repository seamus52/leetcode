from collections import deque
# intuition:
# BFS, for each cell:
# 1) enqueue each cell underneath, if cell is at the start of the row
# 2) enqueue every (right) adjacent cell
class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        q = deque([(0, 0)])
        collector = []

        while q:
            r, c = q.popleft()
            collector.append(nums[r][c])

            if c == 0 and r + 1 < len(nums):
                q.append((r + 1, c))

            if c + 1 < len(nums[r]):
                q.append((r, c + 1))

        return collector
