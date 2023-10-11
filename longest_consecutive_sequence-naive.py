# push onto heap
# scan for max consecutive

# time: O(n * log(n))
# space: O(n)
# essentially this solution is the same as sorting - lot of effort for little gain

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0: # edge case
            return 0

        h = []
        heapify(h)
        for n in nums:
            heappush(h, n)

        cnt = 0
        max_cnt = 0
        prev = h[0] - 1

        for i in range(len(h)):
            e = heappop(h)

            if e == prev: # edge case
                continue
            
            if e == prev + 1:
                cnt += 1
            else:
                cnt = 1
            
            if cnt > max_cnt:
                max_cnt = cnt
            
            prev = e
            # print(e, prev, cnt, max_cnt)
                
        return max_cnt
