# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# time: O(n)
# space: O(1)
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def isMirror(tree1, tree2):
            if not tree1 or not tree2: # if one of them is null
                return tree2 == tree1  # compare them
            if tree1.val != tree2.val: # if above not executed, means they are both number
                return False           # if they are both different return false
                                       # if they are similar go and look further
            return isMirror(tree1.left, tree2.right) and isMirror(tree1.right, tree2.left)
        
        if not root:
            return True
        return isMirror(root.left, root.right)
