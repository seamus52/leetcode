# time: O(log n) - sort will dominate
# space: O(n)
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        intervals.sort(key=lambda x : x[0])

        stack = [intervals[0]]

        for i in range(1, len(intervals)):
            prev_start = stack[-1][0]
            prev_end = stack[-1][1]
            curr_start = intervals[i][0]
            curr_end = intervals[i][1]

            # in case of proper overlap (= no full containment), merge on top of stack
            if curr_start <= prev_end and prev_end < curr_end:
                stack[-1][1] = curr_end
            # in case of total containment, no op
            elif prev_start <= curr_start and curr_end <= prev_end:
                pass # no op
            # otherwise add to collector stack
            else:
                stack.append([curr_start, curr_end])
            
        return stack
