class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []
        for n in nums1:
            i = nums2.index(n)
            larger = -1
            for j in range(i + 1, len(nums2)):
                if nums2[j] > n:
                    larger = nums2[j]
                    break
            ans.append(larger)

        return ans

