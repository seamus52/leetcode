# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# BFS, levels
# traverse into level -> node list dict
# reverse every even list
# return list of levels

# time: O(n) + O(l) / 2 (for reversal)
# space: O(n)
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        def bfs(root, levels):
            if not root:
                return []

            q = deque([(root, 0)])

            while q:
                node, level = q.popleft()

                if level not in levels:
                    levels[level] = []
                levels[level].append(node.val)
                if node.left:
                    q.append((node.left, level + 1))
                if node.right:
                    q.append((node.right, level + 1))

        levels = {}
        bfs(root, levels)

        levels_zigzagged = []
        for l in levels:
            if l % 2 == 0: # keeping 0-indexing in mind
                levels_zigzagged.append(levels[l])
            else:
                levels_zigzagged.append(levels[l][::-1])

        return levels_zigzagged
