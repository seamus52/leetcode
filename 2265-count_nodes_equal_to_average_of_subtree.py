# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        def dfs(root):
            nonlocal acc
            if not root:
                return 0, 0  # tuple: sum, count

            l_sum, l_count = dfs(root.left)
            r_sum, r_count = dfs(root.right)
            n_sum = l_sum + root.val + r_sum
            n_count = l_count + 1 + r_count

            if n_sum // n_count == root.val:
                acc += 1

            return n_sum, n_count

        acc = 0
        dfs(root)
        return acc
