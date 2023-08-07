# build adjacency matrix
# criteria to test:
# 1) graph has no cycles -> constraints guarantee that there is no repeated edges -> # of edges <= num of nodes (in other words, num of edges = n)
# 2) all nodes can be visited -> trivial: track
# 3) there is only 1 connected component
# logic
# - if # of edges > # of > nodes, return false
# - build adj list - put in all edge paids (undirected)
# - traverse from arbitrary starting point
# - if there are unvisited nodes, return false

# time: O(n)
# space: O(n)

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # TODO cover edge cases - empty list, n = 0, etc
        if n - 1 != len(edges):
            return False

        graph = self.build_graph(edges, n)
        visited = set()
        self.traverse(graph, 0, visited)

        if len(visited) != n:
            return False

        return True

    
    def traverse(self, graph, node, visited):
        if node in visited:
            return
        
        visited.add(node)
        for neigbor in graph[node]:
            if neigbor not in visited:
                self.traverse(graph, neigbor, visited)

    def build_graph(self, edges, n):
        graph = {}
        for i in range(n):
            graph[i] = set()
        
        for k, l in edges:
            graph[k].add(l)
            graph[l].add(k)

        return graph

