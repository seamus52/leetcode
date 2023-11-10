from collections import Counter, defaultdict
# no need to worry about duplicates: the constraints guarantee there will be no
# [1, 4] and [4, 1] at the same time
# time: O(n)
# space O(n)
class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        freq = Counter() # freq count: input for identifying endpoints
        graph = defaultdict(list)
        for t in adjacentPairs: # build graph
            a, b = t
            graph[a].append(b)
            graph[b].append(a)
            freq[b] += 1
            freq[a] += 1

        
        # find endpoint(s)
        endpoints = []
        for k, v in freq.items():
            if v == 1:
                endpoints.append(k)

        # traverse
        arr = []
        visited = set()
        node = endpoints[0]
        while node not in visited:
            arr.append(node)
            visited.add(node)
            for nbr in graph[node]:
                if nbr not in visited:
                    node = nbr

        return arr
