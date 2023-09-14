# time: O(n)
# space: O(n) - distinct values in tasks, more specifically
from collections import Counter
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = Counter(tasks)

        max_freq = max(freq.values())
        tasks_w_max_freq = list(freq.values()).count(max_freq)

        # case 1: not enough slots, there will be some idling
        # terms explained:
        # n + 1: full workload cycle (idle + busy time)
        # max_freq - 1: the last task doesn't have to idle
        # + tasks_w_max_freq: account for busy time of last tasks
        c1 = (n + 1) * (max_freq - 1) + tasks_w_max_freq
        
        # case 2: enough slots, no idling is needed
        c2 = len(tasks)

        return max(c1, c2)
