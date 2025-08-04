class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        dp = [[-1 for _ in range(amount+1)] for _ in range(n)]

        def make_pair(i, amount):
            if amount == 0:
                return 1
            if i == 0:
                if coins[i] <= amount and amount%coins[i] == 0:
                    return 1
                else:
                    return 0

            if dp[i][amount] != -1:
                return dp[i][amount]
            pick = 0
            if coins[i] <= amount:
                pick = make_pair(i, amount-coins[i])

            not_pick = make_pair(i-1, amount)
            dp[i][amount] = pick + not_pick
            return dp[i][amount]
        
        tot_ways = make_pair(n-1, amount)
        if tot_ways:
            return tot_ways
        return 0