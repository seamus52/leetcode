class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n = len(nums[0])
        threshold = 2 ** n
        nums_set = set(nums)
        # print(threshold)
        for num in range(threshold):
            bin_num = bin(num)[2:] 
            if "0" * (n - len(bin_num)) + bin_num not in nums_set:
                return "0" * (n - len(bin_num)) + bin_num

