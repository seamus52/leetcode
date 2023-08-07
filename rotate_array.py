class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # own solution
        # time: O(k*n)
        # space: O(1)
        # for i in range(k):
        #     n = nums.pop()
        #     nums.insert(0, n)
        #     # print(nums)

        # own solution enhanced
        # time: O(n)
        # space: O(n)
        q = deque(nums)
        for i in range(k):
            q.insert(0, q.pop())
            # print(nums)
        nums[:] = q

        # expressive solution:
        # k %= len(nums)
        # nums[k:], nums[:k] = nums[:-k], nums[-k:]

        # brute force:
        # k %= len(nums) # speed up the rotation
        # for i in range(k):
        #     previous = nums[-1]
        #     for j in range(len(nums)):
        #         nums[j], previous = previous, nums[j]

