# time: O(n)
# space: O(n)
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        cnt = 0
        # sum -> cnt, sum of 0 can be produced by not selecting any element
        csum = {0: 1}
        s = 0

        for n in nums:
            s += n
            if s - k in csum:
                cnt += csum[s - k]

            if s in csum:
                csum[s] += 1
            else:
                csum[s] = 1

        return cnt
