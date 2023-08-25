from collections import deque
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        def build_graph():
            graph = defaultdict(list)
            for s, d, p in flights:
                graph[s].append((d, p))

            return graph


        def bfs(graph):
            nonlocal min_cost
            # init with node, price:
            # getting to start from nowehere doesn't cost anything
            q = deque([(src, 0, k + 1)])

            while q:
                node, cost, remain = q.popleft()

                if remain < 0:
                    continue
                
                if node == dst:
                    min_cost = min(min_cost, cost)

                for nbr, ncost in graph[node]:
                    if cost < min_cost:
                        q.append((nbr, cost + ncost, remain - 1))
                    

        graph = build_graph()
        min_cost = float("inf")
        bfs(graph)
        return min_cost if min_cost != float("inf") else -1
