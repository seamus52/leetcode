class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        prev_max = 0
        res = []

        for i in range(len(heights) - 1, -1, -1):
            if heights[i] > prev_max:
                res.append(i)
                prev_max = heights[i]

        return list(reversed(res))

