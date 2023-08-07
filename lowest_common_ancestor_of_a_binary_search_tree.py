# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# problem not very well specified: need to return a TreeNode
# time: avg case O(log n), worst case O(n)
# space: O(n) - stack frames
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        p_collector = []
        p_path = self.find_path(root, p, p_collector)
        q_collector = []
        q_path = self.find_path(root, q, q_collector)

        lowest_common_ancestor = None
        for i in range(min(len(p_collector), len(q_collector))):
            if p_collector[i] == q_collector[i]:
                lowest_common_ancestor = p_collector[i]
            else:
                break

        return lowest_common_ancestor

    def find_path(self, root, node, collector):
        collector.append(root)
        if node.val < root.val:
            self.find_path(root.left, node, collector)
        elif node.val > root.val:
            self.find_path(root.right, node, collector)

        return collector

# A simpler solution
# class Solution:
#     def lowestCommonAncestor(self, root, p, q):
#         """
#         :type root: TreeNode
#         :type p: TreeNode
#         :type q: TreeNode
#         :rtype: TreeNode
#         """
#         # Value of current node or parent node.
#         parent_val = root.val

#         # Value of p
#         p_val = p.val

#         # Value of q
#         q_val = q.val

#         # If both p and q are greater than parent
#         if p_val > parent_val and q_val > parent_val:    
#             return self.lowestCommonAncestor(root.right, p, q)
#         # If both p and q are lesser than parent
#         elif p_val < parent_val and q_val < parent_val:    
#             return self.lowestCommonAncestor(root.left, p, q)
#         # We have found the split point, i.e. the LCA node.
#         else:
#             return root
