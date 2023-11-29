# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def is_valid(root, upper, lower):
            if not root:
                return True

            curr = root.val < upper and root.val > lower
            l = is_valid(root.left, root.val, lower)
            r = is_valid(root.right, upper, root.val)

            return curr and l and r

        return is_valid(root, inf, -inf)

