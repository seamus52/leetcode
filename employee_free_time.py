"""
# Definition for an Interval.
class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end
"""
# time: O(n)
# space: O(n)
class Solution:
    def merge_intervals(self, intervals):
        merged = [intervals[0]]
        
        for current in intervals[1:]:
            prev = merged[-1] 
            if current.start > prev.end:
                merged.append(current)
            else:
                if current.end > prev.end:
                    prev.end = current.end

        return merged


    def find_gaps(self, merged_schedule):
        free_time = []
        prev = merged_schedule[0]
        for curr in merged_schedule[1:]:
            free_time.append(Interval(prev.end, curr.start))
            prev = curr

        return free_time


    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        # unpack
        flat_schedule = []
        for s in schedule:
            flat_schedule += [*s]
        
        # sort intervals by start time
        flat_schedule.sort(key=lambda x : x.start)

        # merge intervals
        merged_schedule = self.merge_intervals(flat_schedule)
        [print(x.start, x.end) for x in merged_schedule]

        # process & return
        return self.find_gaps(merged_schedule)
