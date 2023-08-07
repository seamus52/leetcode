# time O(n log n) - which is a bit worse than spec
# space O(n)
from heapq import heapify, heappush, heappop
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # nums_sorted = []
        # heapify(nums_sorted)
        # for n in nums:
        #     heappush(nums_sorted, -n)

        # for x in range(k - 1):
        #     heappop(nums_sorted)

        # return -heappop(nums_sorted)

        # does all the above as 1-liner
        return heapq.nlargest(k, nums)[-1]
