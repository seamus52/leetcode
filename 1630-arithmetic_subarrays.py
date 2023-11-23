# time: O(m * n * log n)
# space: O(1)
class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        collector = []
        for s, e in zip(l, r):
            slice = sorted(nums[s:e + 1])
            diff = slice[1] - slice[0]
            for i in range(1, len(slice)):
                if slice[i] - slice[i - 1] != diff:
                    collector.append(False)
                    break
            else:
                collector.append(True)

        return collector

