from collections import Counter
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        c1 = Counter(nums1)
        c2 = Counter(nums2)

        merged = c1 & c2
        ans = []
        for k, v in merged.items():
            ans.extend([k] * v)

        return ans

