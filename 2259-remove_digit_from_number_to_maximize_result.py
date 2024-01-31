class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        positions = []

        for i in range(len(number)):
            if number[i] == digit:
                positions.append(i)

        candidates = []
        for p in positions:
            candidates.append(number[:p] + number[p + 1:])
        # print(candidates)


        max_candidate = candidates[0]
        for c in candidates:
            if int(c) > int(max_candidate):
                max_candidate = c

        return max_candidate
        
