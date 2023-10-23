# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def lca(root, p, q):
            if not root or root == p or root == q:
                return root

            l = lca(root.left, p, q)
            r = lca(root.right, p, q)

            return root if l and r else l or r
                
        return lca(root, p, q)
