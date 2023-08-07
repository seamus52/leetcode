# Time: O(n log n)
# Space: O(n)

class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        # merge arrays into tuples and sort by start time
        jobs = sorted(zip(startTime, endTime, profit), key=lambda x:x[0])
        # extract start times
        starts = [j[0] for j in jobs]
    
        @lru_cache(maxsize=None)
        def max_profit(i):
            if i == len(jobs):
                return 0

            # next_index = after end time of current job (find in starts)
            next_index = bisect.bisect_left(starts, jobs[i][1])

            # return max of:
            # - profit of tree rooted in i + 1
            # - profit of current node + max_profit(calculated next_index)
            return max(max_profit(i + 1), jobs[i][2] + max_profit(next_index))
        
        return max_profit(0)
