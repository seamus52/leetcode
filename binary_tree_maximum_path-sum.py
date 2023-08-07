# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_sum = [float("-inf")] # could use nonlocal + nesting

        self.traverse(root, max_sum)

        return max_sum[0]

    def traverse(self, root, max_sum):
        if not root:
            return 0

        # if left or right sum are negative, they are counted as 0!
        left_sum = max(self.traverse(root.left, max_sum), 0)
        right_sum = max(self.traverse(root.right, max_sum), 0)

        left_candidate = left_sum + root.val
        right_candidate = right_sum + root.val
        full_candidate = left_sum + root.val + right_sum
        
        max_sum[0] = max(root.val, left_candidate, right_candidate, full_candidate, max_sum[0])

        return max(left_candidate, right_candidate)
