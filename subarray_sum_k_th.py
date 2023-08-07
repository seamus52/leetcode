# time: O(n)
# space: O(n)
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        cnt = 0
        s = 0
        m = defaultdict(int)
        m[0] = 1
        for i in range(len(nums)):
            s += nums[i]
            if s - k in m:
                cnt += m[s - k];
            m[s] = m[s] + 1

        return cnt
