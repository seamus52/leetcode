# slide the window, add/remove items on the go for each step
# be mindful of boundaries

# Naive -> TLE
# finding max is costly, even w/ minor optimization (below)
# time (O(n^2))-ish worst case, if the window tends to be large
# space (O(n)), n = number of times sliding window fits

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l = 1
        r = k - 1
        win = deque(nums[0:k])
        win_max = max(win)
        collector = [win_max]

        while r < len(nums) - 1:
            # move window bounds
            r += 1
            l += 1
            # update window content
            leaving = win.popleft()
            win.append(nums[r])
            # update max - minor optimization to call max(win) less frequently
            if nums[r] > win_max:
                win_max = max(win)
            if leaving == win_max:
                win_max = max(win)
            # collect max
            collector.append(win_max)
            
        return collector
