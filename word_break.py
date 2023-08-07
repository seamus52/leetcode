# time: O(N*M*len(dict)) ~ cubic
# space: O(n^2)
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        words = set(wordDict) # for faster containment checks
        q = deque([0])
        visited = set()

        while q:
            start = q.popleft()
            # visited.add(start) # optimization needed

            if start == len(s):
                return True

            for end in range(start + 1, len(s) + 1):
                if end in visited: continue

                if s[start:end] in words:
                    q.append(end)
                    visited.add(end) # time optimization for visited

        return False

