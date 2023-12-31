# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def max_path(root):
            nonlocal max_sum
            if not root:
                return 0

            l = max(max_path(root.left), 0)
            r = max(max_path(root.right), 0)
            l_candidate = l + root.val
            r_candidate = r + root.val
            full_candidate = l + root.val + r

            max_sum = max(max_sum, root.val, full_candidate)

            return root.val + max(r, l)


        max_sum = -inf
        max_path(root)
        return max_sum

        
