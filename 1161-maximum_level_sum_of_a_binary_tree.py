# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        max_level = 1
        max_level_sum = -inf
        q = deque([(root, 1)])

        while q:
            level_len = len(q)
            level_sum = 0

            for _ in range(level_len):
                node, curr_level = q.popleft()

                level_sum += node.val

                if node.left:
                    q.append((node.left, curr_level + 1))
                if node.right:
                    q.append((node.right, curr_level + 1))

            if level_sum > max_level_sum:
                max_level_sum = level_sum
                max_level = curr_level

        return max_level
    
