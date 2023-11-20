# time: O(n) - not real N^2 due to pop happens 1x at max
# space O(n)
# solution uses monotinic stack
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        s = [] # monotinic stack
        waits = [0] * len(temperatures)

        for curr_day_idx, t in enumerate(temperatures):
            # remove all entries in stack that refer to items that are
            # smaller than the current temperature
            while s and t > temperatures[s[-1]]:
                prev_day_idx = s.pop()
                # calculate wait duration from diff between days
                waits[prev_day_idx] = curr_day_idx - prev_day_idx
            s.append(curr_day_idx)

        return waits
