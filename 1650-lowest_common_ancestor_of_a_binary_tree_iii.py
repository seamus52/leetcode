"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        def find_root(node):
            if not node.parent:
                return node

            return find_root(node.parent)

        def dfs(root, target, path, collector):
            if root == target:
                collector.append(path[:] + [root])
                return

            path.append(root)
            if root.left:
                dfs(root.left, target, path, collector)
            if root.right:
                dfs(root.right, target, path, collector)

        def lca(root, p, q):
            if not root or root == p or root == q:
                return root

            l = lca(root.left, p, q)
            r = lca(root.right, p, q)

            return root if l and r else l or r

        root = find_root(p)
        # print(root.val)

        return lca(root, p, q)
