# time: O(cities + flights * steps)
# space: O(cities + flights * steps)
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        def build_graph(n, flights):
            graph = {}
            for i in range(n):
                graph[i] = set()
            for s, d, p in flights:
                graph[s].add((d, p))
            return graph

        @lru_cache(maxsize=None)
        def dfs(s, d, p, steps):
            nonlocal cheapest

            if d == dst:
                cheapest = min(p, cheapest)

            for next, price in graph[d]:
                # prune impossible paths early
                if p + price < cheapest and steps > 0:
                    dfs(d, next, p + price, steps - 1)

        cheapest = inf
        graph = build_graph(n, flights)

        dfs(None, src, 0, k + 1)

        return cheapest if cheapest != inf else -1
