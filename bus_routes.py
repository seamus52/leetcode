# N: # of routes; bi: # of stops on the ith route
# time: O(∑(N−i)bi)
# space: O(∑(N−i)b)

from collections import deque
class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        station_to_route = defaultdict(set)
        for route_idx, route in enumerate(routes):
            for station in route:
                station_to_route[station].add(route_idx)

        # BFS for shortest path
        cnt = -1
        visited = set()
        
        q = deque()
        q.append(source)
        
        while q:
            cnt += 1
            for _ in range(len(q)):
                curr_station = q.popleft()
                if curr_station == target:
                    return cnt
                for route_idx in station_to_route[curr_station]:
                    if route_idx not in visited:
                        visited.add(route_idx) # visited optimalization
                        q.extend(routes[route_idx])
        return -1
