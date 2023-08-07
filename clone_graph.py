"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

# copy nodes into another graph, and just return the same entry node, NOT an adjacency list
# pythonic solution:
# return deepcopy(node) 

# e = number of edges
# v = number of vertices
# time: O(e*v)
# space: O(v)
from collections import deque
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return node

        # dict will track visited and allow for easy lookup of cloned nodes by original nodes
        visited = {}
        q = deque([node])
        visited[node] = Node(node.val, [])

        # n = node (so that we can leave the 'node' parameter intact)
        # m = neighbor 
        while q:
            n = q.popleft()
            for m in n.neighbors:
                if m not in visited:
                    #ensure that an entry exists for every neighbor encountered
                    visited[m] = Node(m.val, [])
                    q.append(m)
                # add cloned version of neighbor to neighbors of cloned version of current node
                visited[n].neighbors.append(visited[m])

        # locate cloned counterpart of original 'head' node
        return visited[node]
