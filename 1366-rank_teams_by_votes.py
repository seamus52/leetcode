class Solution:
    def rankTeams(self, votes: List[str]) -> str:
        teamVotes = collections.defaultdict(lambda: [0] * 26)
        
        for vote in votes:
            for pos, team in enumerate(vote):
                teamVotes[team][pos] += 1

        # for k, v in teamVotes.items():
        #     print(k, v)
        
        return ''.join(sorted(teamVotes.keys(), reverse=True,
            key=lambda team: (teamVotes[team], -ord(team))))

