# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# time: O(nodes * edges)
# space: O(n/2)

# optimization idea: store parent along with node
# manipulate parent when node is found
from collections import deque
class Solution:
    def correctBinaryTree(self, root: TreeNode) -> TreeNode:
        def find_bfs(root):
            q = deque([(root)])
            node_to_remove = None

            while q:
                level_width = len(q)
                level = []
                for _ in range(level_width):
                    n = q.popleft()
                    level.append(n)

                    if n.left:
                        q.append(n.left)
                    if n.right:
                        q.append(n.right)
                
                print([n.val for n in level])
                for i, n in enumerate(level):
                    if n.right in level:
                        return n

        def remove_dfs(root, node_to_remove):
            if not root:
                return

            if root.left:
                if root.left == node_to_remove:
                    root.left = None
                else:
                    remove_dfs(root.left, node_to_remove)

            if root.right:
                if root.right == node_to_remove:
                    root.right = None
                else:
                    remove_dfs(root.right, node_to_remove)

        n = find_bfs(root)
        print(n.val)
        remove_dfs(root, n)

        return root
   
