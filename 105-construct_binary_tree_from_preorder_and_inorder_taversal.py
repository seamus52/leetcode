# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# time: O(N^2)
# space O(N) - recursive stack for a highly unbalanced tree (not counting output)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# time: O(N^2)
# space O(N) - recursive stack for a highly unbalanced tree (not counting output)
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not inorder:  # Base case for stopping recursion
            return None

        # Find index of root node ('s value) within inorder
        # and remove node from inorder.
        # Front of preorder holds root's value, consume one node at a time
        inorder_idx = inorder.index(preorder.pop(0))
        root = TreeNode(inorder[inorder_idx])

        # Recursively generate left subtree starting from
        # 0th index to root index within inorder
        root.left = self.buildTree(preorder, inorder[:inorder_idx])

        # Recursively generate right subtree starting from
        # next of root index till last index
        root.right = self.buildTree(preorder, inorder[inorder_idx + 1:])

        return root
