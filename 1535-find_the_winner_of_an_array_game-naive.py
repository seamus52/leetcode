from collections import deque, defaultdict
class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        q = deque(arr)
        winners = defaultdict(int)

        while True:
            a = q.popleft()
            b = q.popleft()

            winners[max(a, b)] += 1
            # print(a, b, max(a, b), winners[max(a, b)])
            if winners[max(a, b)] == k:
                return max(a, b)

            q.appendleft(max(a, b))
            q.append(min(a, b))

        return 666
