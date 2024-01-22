# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def is_valid(root, lower, upper):
            if not root:
                return True

            curr = lower < root.val < upper
            l = is_valid(root.left, lower, root.val)
            r = is_valid(root.right, root.val, upper)
            return curr and l and r

        return is_valid(root, -inf, inf)

