# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        q = deque([(root, 0)])

        while q:
            level = []

            for _ in range(len(q)):
                node, l = q.popleft()

                # early termination
                if l % 2 == 0 and node.val % 2 == 0:
                    return False
                elif l % 2 == 1 and node.val % 2 == 1:
                    return False

                level.append(node.val)

                if node.left:
                    q.append((node.left, l + 1))
                if node.right:
                    q.append((node.right, l + 1))

            if l % 2 == 0:
                for i in range(1, len(level)):
                    if level[i - 1] >= level[i]:
                        return False
            else:
                for i in range(1, len(level)):
                    if level[i - 1] <= level[i]:
                        return False

            print(level)

        return True

