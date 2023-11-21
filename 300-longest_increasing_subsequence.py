# time: O(n log n)
# space: O(n)
from bisect import bisect_left
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        sub = []
        for n in nums:
            insert_pos = bisect_left(sub, n)
            if insert_pos == len(sub):
                sub.append(n)
            else:
                sub[insert_pos] = n

        return len(sub)
        
