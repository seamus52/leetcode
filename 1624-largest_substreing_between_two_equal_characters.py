# time: O(n)
# space: O(n)
from collections import defaultdict
class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        d = defaultdict(list)

        for i, c in enumerate(s):
            d[c].append(i)

        max_dist = -1
        for dist in d.values():
            if len(dist) > 1:
                max_dist = max(max_dist, dist[-1] - dist[0] - 1)

        return max_dist

