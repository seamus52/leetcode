# time: O(n log n)
# space: O(m)
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        # Sort the meetings in increasing order of their start time
        intervals.sort(key= lambda x: x[0])

        # Heap stores meeting ends
        rooms = []        
        # Add the first meeting: we need at least 1 room
        heapq.heappush(free_rooms, intervals[0][1])

        # For all the remaining meetings
        for i in intervals[1:]:
            # if a room is freed up before the next meeting start
            if free_rooms[0] <= i[0]:
                heapq.heappop(free_rooms) # remove freed up room
            # add end time of subsequent meeting
            heapq.heappush(free_rooms, i[1])

        # size of heap = minimum rooms required for all meetings
        return len(free_rooms)

