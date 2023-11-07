# time: O(n log n) - sort dominates
# space: O(n)
from functools import cmp_to_key
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def cust_comp(a, b):
            if a + b > b + a:
                return 1
            if a + b < b + a:
                return -1
            return 0

        nums_as_str = [str(n) for n in nums]
        nums_sorted = sorted(nums_as_str, key=cmp_to_key(cust_comp), reverse=True)

        return "".join(nums_sorted) if nums_sorted[0] != "0" else "0"
        
