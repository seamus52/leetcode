class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        nums_sum = sum(nums)
        if nums_sum % 2 == 1:
            return False

        """
        dp array keeps track of whether we have seen a particular sum, up to sum_nums
        dp[0] = True; if we never select any element, the total sum is 0.
        """
        dp = [True] + [False] * nums_sum
        for n in nums:
            for curr_sum in range(nums_sum, n - 1, -1):  # avoid going out-of-bounds
                """
                Case 1: curr_sum was seen before.
                        Then, if we don't select the current element, the sum will not change.
						So, this total sum will still exist, and its dp value remains True.
				
				Case 2: curr_sum was not seen before,
				        but it can be obtained by selecting the current element.
						This means that dp[curr - num] = True, and thus dp[curr] now becomes True.
				
				Case 3: curr_sum was not seen before,
				        and it cannot be obtained by selecting the current element.
						So, this sum will still not exist, and its dp value remains False.
                """
                dp[curr_sum] = dp[curr_sum] or dp[curr_sum - n]

        # Finally, we want to obtain the target sum
        return dp[nums_sum // 2]
