# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# time: O(n)
# spec: O(n)
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def dfs(root, collector):
            if not root:
                return

            if not root.left and not root.right:
                collector.append(root.val)
            
            dfs(root.left, collector)
            dfs(root.right, collector)

        c = []
        dfs(root1, c)
        # print(c)
        d = []
        dfs(root2, d)
        # print(d)

        return c == d
