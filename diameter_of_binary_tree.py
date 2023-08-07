# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# time: O(n) recursive call for every node
# space: O(h) stack frames at any given time
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def longest_path(root):
                if not root:
                    return 0

                nonlocal diameter
                # recursively find the longest path in both children
                left_path = longest_path(root.left)
                right_path = longest_path(root.right)

                # update diameter if left_path + right_path is larger
                diameter = max(diameter, left_path + right_path)

                # return longest of left_path and right_path, add 1 for current node
                return 1 + max(left_path, right_path)

        diameter = 0
        longest_path(root)
        return diameter
