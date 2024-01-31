# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(root, max_so_far):
            nonlocal cnt
            if not root:
                return

            if root.val >= max_so_far:
                # print(root.val, max_so_far)
                cnt += 1

            dfs(root.left, max(root.val, max_so_far))
            dfs(root.right, max(root.val, max_so_far))

        cnt = 0
        dfs(root, -inf)
        return cnt

