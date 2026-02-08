class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        memo = {}
        NEG = -10**18

        def dp(i: int, holding: int) -> int:
            if i == n:
                return 0 if holding == 0 else NEG

            key = (i, holding)
            if key in memo:
                return memo[key]

            if holding == 0:
                buy = -prices[i] + dp(i + 1, 1)   # pick: buy
                skip = dp(i + 1, 0)               # not pick
                memo[key] = max(buy, skip)
            else:
                sell = prices[i]                  # pick: sell (end transaction)
                hold = dp(i + 1, 1)               # not pick
                memo[key] = max(sell, hold)

            return memo[key]

        ans = dp(0, 0)
        return max(0, ans)
