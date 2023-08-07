# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# time: O(n)
# space: O(depth) -> stack space
class Solution:
    def kthSmallest(self, root, k):
        def traverse_inorder(root):
            if root:
                return traverse_inorder(root.left) + [root.val] + traverse_inorder(root.right)
            else:
                return []
    
        return traverse_inorder(root)[k - 1]
