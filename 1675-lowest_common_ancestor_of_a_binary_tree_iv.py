class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', nodes: 'List[TreeNode]') -> 'TreeNode':
        nodes = set(nodes)
        
        def dfs(root):
            if not root or root in nodes:
                return root

            l = dfs(root.left)
            r = dfs(root.right)
            
            return root if l and r else l or r
        
        return dfs(root)
