class Solution:
    def frequencySort(self, s: str) -> str:
        c = Counter(s)
        output = ""

        for k, v in sorted(c.items(), key=lambda x : x[1], reverse=True):
            output += v * k

        return output

