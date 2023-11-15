# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = righta
# time: node * node * path
# space: graph depth (recursive call stack)
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        def psum(root, s):
            nonlocal cnt
            if not root:
                return

            s += root.val
            if s == targetSum:
                cnt += 1

            psum(root.left, s)
            psum(root.right, s)

            # s -= root.val

        def dfs(root):
            if not root:
                return

            psum(root, 0)

            dfs(root.left)
            dfs(root.right)

        cnt = 0
        dfs(root)
        return cnt
