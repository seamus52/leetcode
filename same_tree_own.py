# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# time: O(n)
# space: O(n)
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def traverse(p, q):
            nonlocal same
            if not p and not q:
                return

            if not p and q or p and not q:
                same = False
                return

            if p.val != q.val:
                same = False
                return

            traverse(p.left, q.left)
            traverse(p.right, q.right)

        same = True
        traverse(p, q)
        return same
