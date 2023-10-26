# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import Counter
class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        # If the leaf has 0 coins (an excess of -1 from what it needs)
        # , then we should push a coin from its parent onto the leaf.
        # If it has say, 4 coins (an excess of 3), then we should push 3 coins
        # off the leaf. 
        def dfs(node):
            nonlocal moves
            if not node:
                return 0

            l, r = dfs(node.left), dfs(node.right)
            
            # # of moves we make from this node to and from its children 
            moves += abs(l) + abs(r)
            # excess number of coins in/below subtre of this node
            return node.val + l + r - 1

        moves = 0
        dfs(root)
        return moves
