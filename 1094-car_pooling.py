class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        cap_at_ts = []
        for trip in trips:
            cap_at_ts.append([trip[1], trip[0]])  # # of passengers get on at ts
            cap_at_ts.append([trip[2], -trip[0]]) # # of passengers get off at ts

        cap_at_ts.sort()

        curr_cap = 0
        for time, passenger_change in cap_at_ts:
            curr_cap += passenger_change
            if curr_cap > capacity:
                return False

        return True
