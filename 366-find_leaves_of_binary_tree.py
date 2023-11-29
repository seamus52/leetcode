# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        def collect(root):
            if not root.left and not root.right:
                leaves.append(root.val)
                return

            if root.left:
                collect(root.left)
            
            if root.right:
                collect(root.right)

        def peel(root):
            if not root:
                return

            if root.left:
                if not root.left.left and not root.left.right:
                    root.left = None
                else:
                    peel(root.left)

            if root.right:
                if not root.right.left and not root.right.right:
                    root.right = None
                else:
                    peel(root.right)

        collector = []
        while root.left or root.right:
            leaves = []
            collect(root)
            collector.append(leaves[:])
            peel(root)

        collector.append([root.val])
            
        return collector

