from collections import deque
class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        elems = {}
        q = deque()
        s = 0

        max_sum = 0
        for n in nums:
            q.append(n)
            elems.setdefault(n, 0)
            elems[n] += 1
            s += n
            if len(q) == k and len(elems.keys()) == k:
                max_sum = max(s, max_sum)
            if len(q) == k:
                leaving_element = q.popleft()
                s -= leaving_element
                elems[leaving_element] -= 1
                if elems[leaving_element] == 0:
                    del elems[leaving_element]
            
        return max_sum

