class TopVotedCandidate(object):

    def __init__(self, persons, times):
        self.leader_at_time = []
        self.count = collections.defaultdict(int)
        for p, t in zip(persons, times):
            self.count[p] += 1
            cnt = self.count[p]
            while len(self.leader_at_time) <= cnt:
                self.leader_at_time.append([])
            self.leader_at_time[cnt].append((t, p))

    def q(self, t):
        start, end = 1, len(self.leader_at_time)
        while start < end:
            mid = (start + end) // 2
            if self.leader_at_time[mid][0][0] <= t:
                start = mid + 1
            else:
                end = mid
        i = start - 1
        j = bisect.bisect(self.leader_at_time[i], (t, float('inf')))
        return self.leader_at_time[i][j-1][1]
