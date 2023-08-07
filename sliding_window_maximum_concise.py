# time O(n)
# space O(k)
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if k == 1:
            return nums

        # will be maintained as monotonic deque
        q = deque()
        win_maxes = []

        for i, n in enumerate(nums):
            # remove idx of elements < n from top
            while q and nums[q[-1]] < n:
                q.pop()

            # add current idx, order will be maintained by removals
            q.append(i)

            # remove indexes that are outside of window
            if q[0] == i - k:
                q.popleft()

            if i >= k - 1:
                win_maxes.append(nums[q[0]])

        return win_maxes




