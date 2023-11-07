# time: O(n * log n) - sort dominates
# space: O(n)

class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        impact_time = []
        for i in range(len(dist)):
            impact_time.append(ceil(dist[i] / speed[i]))

        # print(impact_time)
        events_chrono = sorted(list(zip(dist, speed, impact_time)), key=lambda x: x[2])
        # print(events_chrono)

        t_elapsed = 0
        for t in range(len(events_chrono)):
            # print(t_elapsed, events_chrono[2])
            if t_elapsed == events_chrono[t][2]:
                return t_elapsed
            t_elapsed += 1

        return len(dist)
    
