"""
Maintain a monotonic deque of the indexes of the largest elements we've seen (good candidates):
- Deque should never point to elements smaller than current element
- Deque should never point to elements outside our sliding window (which can happen, for instance in above example, where the first element is actually the largest element in the array, and clings to the deque until we reach an index outside the window.)

Keep adding curr_element to the deque, it will be addressed by queue maintenance and will keep the qeque in sorted order.

Appending the front of the deque (= max) to the output.
"""
import collections
class Solution(object):
    def maxSlidingWindow(self, nums, k):
        q = collections.deque()
        out = []
        for i, n in enumerate(nums):
            print("i = {}, curr element = {}, q = {} and out = {}".format(i, n, q, out))
            while q and nums[q[-1]] < n:
                q.pop()
                print("\t Popped from q because q has elements and nums[q.top] < curr element")
            q.append(i)
            print("\t Added i to q")
            if q[0] == i - k:
                q.popleft()
                print("\t Popped left from q because it's outside the window's leftmost (i-k)")
            if i>=k-1:
                out.append(nums[q[0]])
            print("\t Append nums[q[0]] = {} to out".format(nums[q[0]]))
        return out
