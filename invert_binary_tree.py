# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# recursive solution
# time: O(n)
# space: O(n) - stack frames
class Solution:
    def _invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return

        if root.left:
            self.invertTree(root.left)
        if root.right:
            self.invertTree(root.right)

        root.right, root.left = root.left, root.right

        return root

# iterative solution: BFS with queue
