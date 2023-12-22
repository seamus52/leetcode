class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        prices.sort()
        purchase = prices[0] + prices[1]
        return money - purchase if money - purchase >= 0 else money

