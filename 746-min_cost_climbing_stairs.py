class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        @lru_cache(maxsize=None)
        def step(i):
            if i >= len(cost):
                return 0
            
            return min(cost[i] + step(i + 1), cost[i] + step(i + 2))

        return min(step(0), step(1))
        
