class Solution:
    def rob(self, nums: List[int]) -> int:
        @lru_cache(maxsize=None)
        def rob(i, arr):
            if i >= len(arr):
                return 0

            return max(arr[i] + rob(i + 2, arr), rob(i + 1, arr))


        if len(nums) == 1:
            return nums[0]

        a = rob(0, tuple(nums[:-1]))
        b = rob(0, tuple(nums[1:]))

        return max(a, b)

