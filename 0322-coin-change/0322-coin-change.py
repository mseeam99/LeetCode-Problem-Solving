class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}

        def recursion(coins, totalAmount):
            if totalAmount in memo:
                return memo[totalAmount]
            if totalAmount < 0:
                return float('inf')
            if totalAmount == 0:
                return 0

            minCoinNeed = float('inf')
            for coin in coins:
                if totalAmount <= amount and coin <= amount:
                    coinNeed = recursion(coins, totalAmount - coin)
                    minCoinNeed = min(minCoinNeed, coinNeed + 1)

            memo[totalAmount] = minCoinNeed
            return minCoinNeed

        val = recursion(coins, amount)
        return val if val != float('inf') else -1
