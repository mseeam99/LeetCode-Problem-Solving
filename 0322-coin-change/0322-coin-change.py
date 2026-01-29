class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        INF = 10**9
        memo = {}

        def dfs(i, rem):

            if rem == amount:
                return 0
                
            if rem > amount or i == len(coins):
                return INF

            if (i, rem) in memo:
                return memo[(i, rem)]

            pick = 1 + dfs(i, rem + coins[i])
            skip = dfs(i + 1, rem)

            memo[(i, rem)] = min(pick, skip)
            return memo[(i, rem)]

        ans = dfs(0, 0)
        return -1 if ans >= INF else ans
