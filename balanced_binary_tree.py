# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#time: O(n log n) - we stop the algorithm is the diff is > 1
#space: O(n) - stack frames
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def depth(root):
            if not root:
                return 0

            return 1 + max(depth(root.left), depth(root.right))

        # print(depth(root))
        if not root:
            return True

        if self.isBalanced(root.left) and self.isBalanced(root.right):
            return abs(depth(root.left) - depth(root.right)) <= 1

        return False
