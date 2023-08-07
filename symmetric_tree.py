# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# mirror right subtree
# traverse both at the same time, compare
# - structure
# - values
# time: O(n)
# space: O(1)
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def mirror(root):
            if not root:
                return

            root.left, root.right = root.right, root.left
            mirror(root.left)
            mirror(root.right)


        def traverse_compare(root1, root2):
            # validate structure
            if not root1 and not root2:
                return True # got to the leaves on both trees at the same time: implies that the tree is symmetrical

            if (root1 and not root2) or (not root1 and root2):
                return False

            # validate values
            if root1.val != root2.val:
                return False
        
            if not (traverse_compare(root1.left, root2.left) and traverse_compare(root1.right, root2.right)):
                return False

            return True


        left = root.left
        right = root.right
        mirror(right)
        return traverse_compare(left, right)
