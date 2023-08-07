# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# time: O(n)
# space: O(n)
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.validate(root)

    def validate(self, node, low=-math.inf, high=math.inf):
        if not node:
            return True

        if node.val <= low or node.val >= high:
            return False

        return self.validate(node.left, low, node.val) and self.validate(node.right, node.val, high)
