class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        def dfs(root):
            nonlocal path
            if not root:
                return

            path += str(root.val)

            if not root.left and root.right:
                path += "()"

            if root.left:
                path += "("
                dfs(root.left)
                path += ")"
            if root.right:
                path += "("
                dfs(root.right)
                path += ")"

        path = ""
        dfs(root)
        return path

