# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# same solution as 236 Lowest Common Ancestor of a Binary Tree
# does not take advantage of BST propery, but works well enough
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def dfs(root, p, q):
            if not root or root == p or root == q:
                return root

            l = dfs(root.left, p, q)
            r = dfs(root.right, p, q)

            return root if l and r else l or r

        return dfs(root, p, q)
