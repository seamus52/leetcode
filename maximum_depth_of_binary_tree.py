# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# increase step counter, at the end, compare with max paths size so far
# time: O(n)
# space: O(1)
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.traverse(root, 0)


    def traverse(self, root, level):
        if not root:
            return level
        
        return max(self.traverse(root.left, level + 1), self.traverse(root.right, level + 1))
