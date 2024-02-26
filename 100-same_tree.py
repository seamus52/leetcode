# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# time: O(min edges(p, q))
# space: O(min edges(p, q)) - recursive calls
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # compare structure:
        # if one node is None, both should be None
        if not p or not q:
            return not p and not q

        # compare values
        if p.val != q.val:
            return False

        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
