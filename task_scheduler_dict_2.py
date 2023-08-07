class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        """
        STRATEGY
        Greedy; schedule the n most common in round-robin fashion.
        "n most common" adjusts as "time" progresses.
        If there are fewer than n distinct tasks in todo, pad to n with idle states.
        """
        todo = Counter(tasks)
        units = 0                   # "Time" units
        n += 1  # cycle length (idle + following) is more convenient
        while todo:
            # Pick the n items with highest count
            ready = todo.most_common(n)
            n_ready = len(ready)
            units += n_ready
            for k, _ in ready:
                if todo[k] > 1:
                    todo[k] -= 1
                else:
                    del todo[k]     # Would go to 0; delete
            if todo:
                # Fill in with idle time as needed
                units += n - n_ready
        return units
