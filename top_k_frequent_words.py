# time: O(n log n)
# space: O(n)

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        # official
        # cnt = Counter(words)
        # return sorted(list(cnt.keys()), key=lambda x: (-cnt[x], x))[:k]

        # heap-based solution
        cnt = Counter(words)
        heap = []
        for word, freq in cnt.items():
            #python uses min heap
            heap.append((-freq, word))
        heapify(heap)

        response = []
        for i in range(k):
            response.append(heappop(heap)[1])

        return response

