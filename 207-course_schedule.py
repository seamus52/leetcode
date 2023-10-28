class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        def build_graph():
            g = {}
            for i in range(numCourses):
                g.setdefault(i, set())
            for a, b in prerequisites:
                g[b].add(a)
            return g

        def dfs(graph, node, gray, black):
            nonlocal cycle
            if node in black:
                return

            if node in gray:
                cycle = True
                return

            gray.add(node)
            for nbr in graph[node]:
                dfs(graph, nbr, gray, black)

            gray.remove(node)
            black.add(node)


        graph = build_graph()
        gray, black = set(), set()
        cycle = False
        for c in range(numCourses):
            dfs(graph, c, gray, black)
            if cycle:
                return False

        return len(black) == numCourses
