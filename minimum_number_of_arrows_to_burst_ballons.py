# time: O(n)
# space: O(n)
# strategy: greedy
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: x[1]) # sort array on end times
        print(points)

        q = deque(points)
        first = q.popleft()
        s = [first]

        while q:
            curr = q.popleft()
            # if the current balloon starts after the end of another one,
            # one needs one more arrow
            if curr[0] > s[-1][1]:
                s.append(curr)

        return len(s)
