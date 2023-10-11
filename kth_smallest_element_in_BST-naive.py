# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# collect values with inorder traversal until exceeding k in length
# time: O(n)
# space: O(depth) -> stack space

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        collector = []
        self.traverse(root, k, collector)

        return collector[k - 1]

    def traverse(self, root, k, collector):
        # print(collector)
        if len(collector) > k:
            return

        if not root:
            return

        self.traverse(root.left, k, collector)

        if len(collector) == 0:
            if not root.left:
                collector.append(root.val)
        else:
            collector.append(root.val)
            
        self.traverse(root.right, k, collector)
