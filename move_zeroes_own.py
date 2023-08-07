# time: O(n) - worse, needs to find each 0
# space: O(1)

# this solution is in place: python doesn't have arrays, lists can be modified in-place
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero_cnt = nums.count(0)
        
        for x in range(zero_cnt):
            nums.remove(0)

        for x in range(zero_cnt):
            nums.append(0)

        return nums
        
