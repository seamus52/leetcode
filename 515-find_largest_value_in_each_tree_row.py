# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# time: sort dominates - O(n log n)
# space: O(n)
from collections import deque
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        q = deque([(0, root)])
        levels = []

        while q:
            level = []
            level_length = len(q)
            for _ in range(level_length):
                l, n = q.popleft()
                level.append(n.val)
                if n.left:
                    q.append((l + 1, n.left))
                if n.right:
                    q.append((l + 1, n.right))
            levels.append(level[:])

        res = []
        for level in levels:
            level.sort()
            res.append(level[-1])

        return res
