# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# BFS
# count level width, return max count
# time: O(n)
# space: O(n)
class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        q = [(0, root)]
        max_width = 0

        while q:
            n = len(q)
            
            # nodes list to store indexes of all nodes at a level
            nodes = []
            for _ in range(n):
                idx, node = q.pop(0)
                nodes.append(idx)
                if node.left:
                    q.append((2 * idx, node.left))
                if node.right:
                    q.append((2 * idx + 1, node.right))
            # max of ans or (rightmost index - leftmost index + 1) for a level
            max_width = max(max_width, max(nodes) - min(nodes) + 1)
        
        return max_width
