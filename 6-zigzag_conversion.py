from collections import deque
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        d = {}
        for i in range(numRows):
            d[i] = []

        q = deque(list(s))

        while q:
            for r in range(numRows):
                if q:
                    d[r].append(q.popleft())

            for r in range(max(numRows - 2, 0), 0, -1):
                if q:
                    d[r].append(q.popleft())

        print(d)
        ans = ""

        for i in range(numRows):
            ans += "".join(d[i])
            
        return ans

