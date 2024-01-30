"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
from collections import deque
class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return None

        q = deque([root])
        levels = []

        while q:
            level_len = len(q)
            level = []

            for _ in range(level_len):
                node = q.popleft()
                level.append(node)

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            levels.append(level[:])

        # print(levels)

        for level in levels:
            if len(level) == 1:
                continue

            for i in range(1, len(level)):
                level[i - 1].next = level[i]
                # print(level[i - 1].next.val)
        
        return root
