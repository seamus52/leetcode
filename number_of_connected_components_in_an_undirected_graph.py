# build graph
# traverse from each node if not visited
# increment counter

# time: O(edges)
# space: O(nodes * edges from node)

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        def build_graph(edges):
            graph = {}
            for i in range(n):
                graph[i] = set()
            for (p, q) in edges:
                graph[p].add(q)
                graph[q].add(p)
            
            return graph

        def traverse(graph, node, visited):
            visited.add(node)

            for neighbor in graph[node]:
                if neighbor not in visited:
                    traverse(graph, neighbor, visited)

        g = build_graph(edges)
        visited = set()
        cnt = 0

        for n in g:
            if n not in visited:
                traverse(g, n, visited)
                cnt += 1

        return cnt
