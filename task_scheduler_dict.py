# units of time between 2 of the same _always_ applies!
from collections import Counter
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # case where there is no cooldown
        if n == 0:
            return len(tasks)

        # dict to store the tasks as well as the count of each task
        d = Counter(tasks)

        # scenario 1: too many cooldown slots which cannot be
        # filled by other tasks. fx of a particular task(s) is too high.
        max_freq = 0
        for task, freq in d.items():
            max_freq = max(max_freq, freq)
        elems_with_max_freq = 0
        for task, freq in d.items():
            if freq == max_freq:
                elems_with_max_freq += 1
        # n + 1 -> task run + idle
        # max_freq - 1 -> 
        scenario_1 = (n + 1) * (max_freq - 1) + elems_with_max_freq

        # scenario 2: no idle slots, time to finish = # of tasks
        scenario_2 = len(tasks)

        return max(scenario_1, scenario_2)
