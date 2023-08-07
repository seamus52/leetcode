# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# DFS, collect path for each, find 1st common from root
# time: O(n) - n: worst case, number of edges
# space: O(n) - dependent on # of nodes to path
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        p_path = []
        q_path = []

        self.find_path(root, p, p_path)
        self.find_path(root, q, q_path)

        p_path = p_path[::-1]
        q_path = q_path[::-1]

        common = []
        for i in range(min(len(p_path), len(q_path))):
            if p_path[i].val == q_path[i].val:
                common.append(p_path[i])
            else:
                break
        
        return common[-1]

    
    def find_path(self, root, node, path):
        if not root:
            return False

        if root.val == node.val:
            path.append(root)
            return True

        for neighbor in (root.left, root.right):
            if self.find_path(neighbor, node, path):
                path.append(root)
                return True
        
        return False
