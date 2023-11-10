# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def is_identical(root, subRoot):
            if not root and not subRoot:
                return True

            if (root and not subRoot) or (not root and subRoot):
                return False

            if root.val != subRoot.val:
                return False

            return is_identical(root.left, subRoot.left) and is_identical(root.right, subRoot.right)

        def dfs(root, subRoot):
            if not root:
                return False
                
            if is_identical(root, subRoot):
                return True

            return dfs(root.left, subRoot) or dfs(root.right, subRoot) 

        return dfs(root, subRoot)
