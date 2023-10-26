# uses topological sort
# time: O(V+E)
# space: O(V+E)

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        def build_graph(edge_list, num_edges):
            graph = {}
            for e in range(num_edges):
                graph[e] = set()
            for (a, b) in prerequisites:
                graph[b].add(a)

            return graph

        # topological sort + cycle detect w/ WGB
        def traverse(graph, node, collector, gray, black):
            nonlocal cycle
            if node in black:
                return

            if node in gray:
                cycle = True
                return

            gray.add(node)
            for nbr in graph[node]:
                traverse(graph, nbr, collector, gray, black)
           
            gray.remove(node)
            black.add(node)
            collector.append(node)

        # collect
        graph = build_graph(prerequisites, numCourses)
        collector = []
        gray, black = set(), set()
        cycle = False

        for node in graph:
            traverse(graph, node, collector, gray, black)
            if cycle: return []

        return collector[::-1] # correct topological order

