from collections import deque, defaultdict
class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        
        d = defaultdict(set)
        for i, e in enumerate(manager):
            if manager[i] != -1:
                d[e].add(i)

        t = 0
        q = deque([(headID, 0)])  # informing the top manager takes 0 time
        while q:
            parent, time = q.popleft()
            t = max(t, time)
            for child in d[node]:
                # for each level in the graph, the longest notification time
                # will decide the overall min. notification time
                q.append((child, time + informTime[parent]))
            
        return t

