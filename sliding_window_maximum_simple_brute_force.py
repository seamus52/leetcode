from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        win = deque(nums[:k], maxlen=k)
        max_win = [max(win)]

        for n in nums[k:]:
            win.append(n)
            max_win.append(max(win))

        return max_win
