# time: O(number of nodes)
# space: O(number of nodes)
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        def build_graph(edges):
            graph = {}
            for i in range(n):
                graph[i] = []
            for e, f in edges:
                graph[e].append(f)
                graph[f].append(e)
                
            return graph


        def collect_leaves(graph):
            leaves = set()
            for node, neighbors in graph.items():
                if len(neighbors) == 1:
                    leaves.add(node)

            return leaves


        def trim_leaves(graph, leaves):
            for leaf in leaves:
                parent = graph[leaf][0]
                graph[parent].remove(leaf)
                del graph[leaf]


        graph = build_graph(edges)
        print(graph)

        # MHT has 1 or 2 centroids
        while len(graph) > 2:
            leaves = collect_leaves(graph)
            print(leaves)
            trim_leaves(graph, leaves)

        return graph
