# time: O(n^2)
# space: O(n)

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        wc = Counter(words)

        solution = []
        counts = sorted(list(set(wc.values())), reverse=True)
        
        for c in counts:
            words_of_count_c = []
            for w in wc:
                if wc[w] == c:
                    words_of_count_c.append(w)
            words_of_count_c.sort()
            solution += words_of_count_c
            if len(solution) == k:
                break
        
        return solution[:k]
