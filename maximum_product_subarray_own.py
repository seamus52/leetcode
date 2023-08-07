# math.prod()
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_product = nums[0]
        for l in self.segment(nums):
            max_product = max(max_product, self.max_product(l))
        
        if 0 in nums:
            return max(0, max_product)
        else:
            return max_product


    def segment(self, nums):
        segments = []
        segment = []
        for n in nums:
            if n != 0:
                segment.append(n)
            else:
                if len(segment) > 0:
                    segments.append(segment)
                segment = []

        if len(segment) > 0:
            segments.append(segment)

        return segments


    def max_product(self, nums):
        if len(nums) == 1:
            return nums[0]
        max_product = float("-inf")

        for i in range(len(nums)):
            for j in range(i + 1, len(nums) + 1):
                p = math.prod(nums[i:j]) 
                max_product = max(max_product, p)

        return max_product
