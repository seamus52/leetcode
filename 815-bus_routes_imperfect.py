# graph problem
# create adj list
# DFS traverse and find target, return distance length or -1 if target not found
# PROBLEM: solution doesn't distinguish between neighbor on same route (dist = 0) and neighbor on different route

class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        def create_graph(routes):
            graph = {}
            for route in routes:
                for station in route:
                    if station not in routes:
                        graph[station] = set(route)
                        graph[station].remove(station)

            return graph


        def bfs(graph, source, target):
            q = deque([(source, 0)])
            visited = set()

            while q:
                node, distance = q.popleft()
                visited.add(node)
                if node == target:
                    return distance
                
                for nbr in graph[node]:
                    if nbr not in visited:
                        q.append((nbr, distance + 1))

            return -1

        graph = create_graph(routes)
        print(graph)
        return bfs(graph, source, target)
