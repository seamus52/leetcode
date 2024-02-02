# Definition for an infinite stream.
# class InfiniteStream:
#     def next(self) -> int:
#         pass
from collections import deque
class Solution:
    def findPattern(self, stream: Optional['InfiniteStream'], pattern: List[int]) -> int:
        curr_idx = 0
        q = deque()

        for _ in range(len(pattern)):
            q.append(stream.next())

        while True:
            if list(q) == pattern:
                return curr_idx
            q.popleft()
            q.append(stream.next())

            curr_idx += 1
            # print(s, pattern)

