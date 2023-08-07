# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 1) Create graph
# 2) BFS
# time: O(2 * edges)
# space: O(vertices*edges)
class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        def build_graph(root, parent):
            nonlocal graph
            if not root: return

            graph[root.val] = set()
            if parent:
                graph[root.val].add(parent.val)
            if root.left:
                graph[root.val].add(root.left.val)
                build_graph(root.left, root)
            if root.right:
                graph[root.val].add(root.right.val)
                build_graph(root.right, root)

        graph = {}
        build_graph(root, None)
        print(graph)

        q = deque([(target.val, k)])
        k_away = []
        visited = set()

        while q:
            n, level = q.popleft()
            visited.add(n)
            if level == 0:
                k_away.append(n)

            for nbr in graph[n]:
                if nbr not in visited:
                    q.append((nbr, level - 1))

        return k_away
