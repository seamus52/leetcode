# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# time: O(n^2)
# space: O(n)

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        path = []
        paths = []

        self.traverse(root, targetSum, path, paths)

        return paths

    def traverse(self, root, target_sum, path, paths):
        if not root:
            return

        if not root.left and not root.right:
            path.append(root.val)
            if sum(path) == target_sum:
                paths.append(path[:])
            path.pop()
            return

        path.append(root.val)
        if root.left:
            self.traverse(root.left, target_sum, path, paths)
        if root.right:
            self.traverse(root.right, target_sum, path, paths)

        path.pop()
        return
