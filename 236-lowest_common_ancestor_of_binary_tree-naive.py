# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # collect path to p and q
        def dfs(root, path):
            if not root:
                return

            path.append(root)

            if root.val in (p.val, q.val):
                paths.append(path[:])
            
            dfs(root.left, path)
            dfs(root.right, path)
            
            path.pop()
        
        paths = []
        dfs(root, [])

        
        common = []
        for i in range(min(len(paths[0]), len(paths[1]))):
            if paths[0][i] == paths[1][i]:
                common.append(paths[0][i])
            else:
                break

        return common[-1]
        
