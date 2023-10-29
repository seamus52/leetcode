from collections import deque, defaultdict
class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        
        d = defaultdict(set)
        for i, e in enumerate(manager):
            if manager[i] != -1:
                d[e].add(i)

        t = 0
        q = deque([(headID, 0)])
        while q:
            node, time = q.popleft()
            t = max(t, time)
            for nbr_node in d[node]:
                q.append((nbr_node, time + informTime[node]))
            
        return t

