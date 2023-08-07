# counter, fill back according to count
# follow-up: review sort algorithms
# time: O(n)
# space: O(1)-ish (minimal constant extra memory for dict)
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        stats = Counter(nums)
        i = 0
        for color in range(3): # fore every color in order
            for streak in range(stats[color]): # iterate times of its occurrence in the original dataset as shown by the collector
                nums[i] = color
                i += 1
