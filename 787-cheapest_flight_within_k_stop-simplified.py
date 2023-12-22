# time: O(N{cities} + E{flights} * k)
# space: O(N{cities} + E{flights} * k)
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # build graph
        g = {}
        for i in range(n):
            g.setdefault(i, set())
        for s, d, p in flights:
            g[s].add((d, p))


        @lru_cache(maxsize=None)
        def dfs(curr, price, steps):
            nonlocal min_price
        
            if curr == dst:
                min_price = min(min_price, price)

            for nd, np in g[curr]:
                if price + np < min_price and steps < k:
                    dfs(nd, price + np, steps + 1)
            
        min_price = inf
        
        dfs(src, 0, -1)

        return min_price if min_price < inf else -1

