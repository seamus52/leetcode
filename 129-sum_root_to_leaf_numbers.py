# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def dfs(root, path):
            if not root:
                paths.append["0"]
                return

            path.append(str(root.val))

            if not root.left and not root.right:
                paths.append(path[:])
                path.pop()
                return

            if root.left:
                dfs(root.left, path)

            if root.right:
                dfs(root.right, path)

            path.pop()

        paths = []
        dfs(root, [])
        # print(paths)
        s = 0
        for p in paths:
            s += int("".join(p))

        return s
