# time: O(n^2)
# space: O(1) no extra space other than collecting output
class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        def in_bounds(r, c):
            nonlocal max_row_len
            return 0 <= r < len(nums) and 0 <= c < max_row_len and c < len(nums[r])

        if len(nums) == 1:
            return nums[0]
        
        collector = []
        max_row_len = 0
        for row in nums:
            max_row_len = max(max_row_len, len(row))

        for row in range(len(nums)):
            r = row
            for c in range(max_row_len):
                if in_bounds(r, c):
                    collector.append(nums[r][c])
                r -= 1
        
        start = 1
        for _ in range(max_row_len):
            r = len(nums) - 1
            for c in range(start, max_row_len):
                if in_bounds(r, c):
                    collector.append(nums[r][c])
                r -= 1
            start += 1
        
        return collector
        
