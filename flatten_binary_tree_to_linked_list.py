# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def dfs(root, nodes):  # collect nodes into a list
            if not root:
                return

            nodes.append(root)
            dfs(root.left, nodes)
            dfs(root.right, nodes)

        def construct(nodes):
            dummy_head = TreeNode()
            curr = dummy_head
            for n in nodes:
                curr.right = n  # use right pointer as linked list next
                curr.left = None  # disable left ponter
                curr = curr.right

            return dummy_head

        nodes = []
        dfs(root, nodes)
        root = construct(nodes)
