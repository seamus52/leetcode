# Trick: max moves down 1 step of the time.
# From that point, max wins always
# To recognize this, needs to be visualized
# Edge case: if k < len(arr), game needs to be simulated
# time: O(n)
# space: O(n)
from collections import deque
class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        if k >= len(arr):
            return max(arr)
        else:    
            q = deque(arr)
            winners = defaultdict(int)

            for i in range(5 * len(arr)):
                a = q.popleft()
                b = q.popleft()

                winners[max(a, b)] += 1
                # print(a, b, max(a, b), winners[max(a, b)])
                if winners[max(a, b)] == k:
                    return max(a, b)

                q.appendleft(max(a, b))
                q.append(min(a, b))

        return 666
