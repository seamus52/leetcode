# time: O(n)
# space: O(1)
class Solution:
    def maxScore(self, s: str) -> int:
        c = Counter(list(s))
        zeros_seen = ones_seen = left_score = right_score = max_score = 0

        for i in range(len(s) - 1):
            if s[i] == "0":
                zeros_seen += 1
            else:
                ones_seen += 1

            left_score = zeros_seen
            right_score = c["1"] - ones_seen
            
            max_score = max(max_score, left_score + right_score)

        return max_score
        
