# sort by 1st element
# check if there is an interval which has a 1st element between 1st and last of previous element

# time: O(n)
# space: O(1)

class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort(key=lambda x : x[0])
        
        while intervals:
            current = intervals.pop()
            current_start, current_end = current[0], current[1]
            if intervals:
                last_start, last_end = intervals[-1][0], intervals[-1][1]
                if current_start < last_end:
                    return False
        
        return True
