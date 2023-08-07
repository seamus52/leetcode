# time: O(n^2 * k (reversing, comparing)) -> TLE
# space: O(n^2) - ish, worst case
class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        pp = []
        for i, w in enumerate(words):
            for j, x in enumerate(words):
                if i != j:
                    joint = w + x
                    if joint == joint[::-1]:
                        pp.append([i, j])
                else: continue

        return pp
