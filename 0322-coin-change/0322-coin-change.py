class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        coins.sort()

        dp = [0] * (amount + 1)
        for i in range(amount + 1):
            dp[i] = amount + 1
        dp[0] = 0
        
        for i in range(1, amount + 1):
            for coin in coins:
                if coin <= i:
                    dp[i] = min(dp[i], dp[i - coin]+1)
                    
        return dp[-1] if dp[amount] != amount + 1 else -1



        