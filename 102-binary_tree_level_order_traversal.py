# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# time: O(n)
# space: O(n)
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        def traverse(root, level):
            nonlocal collector
            if not root:
                return

            if level not in collector:
                collector[level] = []
            collector[level].append(root.val)

            traverse(root.left, level + 1)
            traverse(root.right, level + 1)

        collector = {}
        traverse(root, 0)

        return [collector[l] for l in collector]

