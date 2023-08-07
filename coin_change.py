#time: O(n^2) with DP (step * n to be precise)
#space: O(n) recursive call stack (n = step, to be precise)
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}
        min_change = self._coinChange(coins, amount, memo)
        if min_change == float("inf"):
            return -1
        else:
            return min_change


    def _coinChange(self, coins: List[int], amount: int, memo) -> int:
        if amount in memo:
            return memo[amount]

        if amount == 0:
            return 0
        if amount < 0:
            return float("inf")

        min_coins = float("inf")
        for c in coins:
            num_coins = 1 + self._coinChange(coins, amount - c, memo)
            min_coins = min(min_coins, num_coins)

        memo[amount] = min_coins
        return min_coins

    # alternative to wrapper call:
    # return memo[amount] if memo[amount] != float('inf') else -1
