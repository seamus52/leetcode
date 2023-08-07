# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# time: O(n)
# space: O(n)
class Solution:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> Optional[TreeNode]:
        def traverse(root, target):
            nonlocal values
            if not root:
                return

            traverse(root.left, target)
            values.append(root.val)
            traverse(root.right, target)

        values = []
        traverse(root, p)
        #print(values)

        if p.val in values:
            idx_of_target = values.index(p.val)
            if idx_of_target != len(values) - 1:
                return TreeNode(values[idx_of_target + 1])
            else:
                return None
            
        else:
            return None

