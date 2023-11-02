from collections import Counter
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = righta
# time: O(nodes * edges)
# space: O(nodes)
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        def dfs(root):
            if not root:
                return
            
            c[root.val] += 1

            dfs(root.left)
            dfs(root.right)

        c = Counter()
        max_items = []
        dfs(root)
        max_cnt = max(c.values())
        for k, v in c.items():
            if v == max_cnt:
                max_items.append(k)
        return max_items
