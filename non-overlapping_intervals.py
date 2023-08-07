# essentially interval merge in disguise w/ a few special cases
# sort, merge (with top of stack), calculate diff
# time: O(n log n) - sort dominates
# space: O(n)
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals_sorted = sorted(intervals, key=lambda x : x[0])
        s = [intervals_sorted[0]]

        for i in range(1, len(intervals)):
            last = s[-1]
            last_start, last_end = s[-1][0], s[-1][1]
            curr = intervals_sorted[i]
            curr_start, curr_end = curr[0], curr[1]

            # new interval falls within last:
            # replace last with new
            if curr_start >= last_start and curr_end <= last_end:
                s.pop()
                s.append(curr)
            # new interval overlaps with last:
            # ignore
            elif curr_start < last_end:
                continue # no op
            # no overlap:
            # append
            else:
                s.append(curr)

        # min # of intervals to remove = diff between stack and original list
        return len(intervals_sorted) - len(s)
