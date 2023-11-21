class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        def rev(n):
            return int(str(n)[::-1])

        cnt = 0
        d = {}
        for num in nums:
            diff = num - rev(num)
            if diff in d:
                d[diff] += 1
                cnt += d[diff]
            else:
                d[diff] = 0
        
        return cnt % (10 ** 9 + 7)
