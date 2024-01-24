class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        res = []
        for i in range(len(nums) // 2):
            res.extend([nums[i], nums[n + i]])

        return res

