# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def lca(root, p, q):
            # both nodes smaller than current: split will be on the left
            if p.val < root.val and q.val < root.val:
                return lca(root.left, p, q)
            # both nodes larger than current: split will be on the right
            if p.val > root.val and q.val > root.val:
                return lca(root.right, p, q)

            # found the split
            return root

        return lca(root, p, q)
