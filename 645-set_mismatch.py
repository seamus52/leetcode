class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        c = Counter(nums)

        ans = [-1, -1]
        for i in range(1, len(nums) + 1):
            if i not in c:
                ans[1] = i
            elif c[i] == 2:
                ans[0] = i

        return ans

