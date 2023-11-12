# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def depth(root):
            if not root:
                return 0

            return 1 + max(depth(root.left), depth(root.right))

        def diameter(root):
            if not root:
                return 0

            l = depth(root.left)
            r = depth(root.right)

            return max(l + r, diameter(root.left), diameter(root.right))

        
        return diameter(root)
