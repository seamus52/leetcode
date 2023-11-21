# intuition:
# nums[i] + rev(nums[j]) == nums[j] + rev(nums[i])
# nums[i] - rev(nums[i]) == nums[j] - rev(nums[j])
# time: O(n)
# space: O(n)
from collections import defaultdict
from math import factorial
class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        def rev(n):
            return int(str(n)[::-1])

        def choose(n, r):
            return factorial(n)//(factorial(r) * factorial(n - r))

        d = defaultdict(set)
        for i, n in enumerate(nums):
            d[n - rev(n)].add(i)

        cnt = 0
        for entry in d.values():
            if len(entry) > 1:
                cnt += choose(len(entry), 2)

        return cnt % (10 ** 9 + 7)

