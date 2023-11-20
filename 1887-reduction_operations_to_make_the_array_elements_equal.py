# time: O(n log n) - sort dominates
# space: O(1)
class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        nums.sort()
        steps = 0  # number of times a value needs to be decreased
        acc = 0  # accummulator of overall decreases

        for i in range (1, len(nums)):
            if nums[i] > nums[i - 1]:
                steps += 1
            acc += steps

        return acc

