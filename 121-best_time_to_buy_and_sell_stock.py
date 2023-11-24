class Solution:
    # brute force:
    # time O(n^2)
    # space O(1)
    # def maxProfit(self, prices: List[int]) -> int:
    #     max_profit = 0
    #     for i in range(len(prices)):
    #         for j in range(i + 1, len(prices)):
    #             if prices[j] - prices[i] > max_profit:
    #                 max_profit = prices[j] - prices[i]

    #     return max_profit

    # time O(n^2)
    # space O(1)
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float("inf")
        max_profit = 0

        for p in prices:
            if p < min_price: # min price needs to preceed sale
                min_price = p
            else:
                max_profit = max(max_profit, p - min_price) # update max_profit if diff w/ current price is more favorable

        return max_profit
