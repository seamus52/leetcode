# find shortest path in weighted graph
# dfs, traverse all paths from source up to k steps, save aggregate path cost upon success, otherwise silently terminate
# return min or -1 if path cost collection is empty
# keeping track of visited may be tricky: try to pop after recursive call(s)

# time: O(nodes*paths)
# space: O(n)
# even w/ prune and visited optimization -> TLE
# perhaps there is a way to speed up w/ DP

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        def build_graph(flights, n):
            graph = {}
            for i in range(n):
                graph[i] = []

            for f in flights:
                s = f[0] # source
                d = f[1] # destination
                p = f[2] # price
                graph[s].append((d, p))
            return graph

        def traverse(graph, src, dst, k, path_cost, visited):
            # print(f"{src}, {dst}, {k}, {path_cost}")
            nonlocal path_costs

            # efficiency optimization: exclude this path if it cannot be minimal
            if len(path_costs) > 0 and path_cost > min(path_costs):
                return

            if src == dst:
                path_costs.append(path_cost)

            if k < 0:
                return

            if src in visited:
                return
            visited.add(src)
            
            for nbr in graph[src]:
                new_src = nbr[0]
                price = nbr[1]
                traverse(graph, new_src, dst, k - 1, path_cost + price, visited)

            visited.remove(src)

        graph = build_graph(flights, n)
        # print(graph)
        path_costs = []
        visited = set()
        traverse(graph, src, dst, k, 0, visited)
        # print(path_costs)

        return min(path_costs) if len(path_costs) > 0 else -1
