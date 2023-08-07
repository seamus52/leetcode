# time: O(n log n) - sort will dominate
# space: O(n)

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        stack = [intervals[0]]

        for i in range(1, len(intervals)):
            prev_start = stack[-1][0]
            prev_end = stack[-1][1]
            curr_start = intervals[i][0]
            curr_end = intervals[i][1]
            if curr_start <= prev_end:
                if prev_end < curr_end:
                    stack[-1] = [prev_start, curr_end]
                else:
                    pass # interval already contained
            else:
                stack.append([curr_start, curr_end])

        return stack
