class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        altitudes = [0]
        max_alt = 0

        for g in gain:
            max_alt = max(max_alt, altitudes[-1] + g)
            altitudes.append(altitudes[-1] + g)
            # print(altitudes)

        return max_alt
