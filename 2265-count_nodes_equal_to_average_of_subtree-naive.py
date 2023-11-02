# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# time: O(n + m)
# space: O(n) + stack frames (tree depth)
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        def dfs_collect(root):
            nonlocal nodes
            if not root:
                return
            nodes.append(root)
            dfs_collect(root.left)
            dfs_collect(root.right)

        def dfs_avg(root):
            nonlocal n_cnt, n_sum
            if not root:
                return

            n_cnt += 1
            n_sum += root.val

            dfs_avg(root.left)
            dfs_avg(root.right)
     
        nodes = []
        dfs_collect(root)
        # [print(n.val) for n in nodes]

        acc = 0
        for n in nodes:
            n_cnt, n_sum  = 0, 0
            dfs_avg(n)
            if n_sum // n_cnt == n.val:
                acc += 1

        return acc
