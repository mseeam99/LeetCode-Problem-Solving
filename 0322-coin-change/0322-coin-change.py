class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        INF = 10**9
        memo = {}

        def dfs(i, rem):
            if rem == 0:
                return 0
            if i == len(coins) or rem < 0:
                return INF

            if (i, rem) in memo:
                return memo[(i, rem)]

            # pick coin i (unlimited -> stay on i)
            pick = 1 + dfs(i, rem - coins[i])

            # skip coin i
            skip = dfs(i + 1, rem)

            memo[(i, rem)] = min(pick, skip)
            return memo[(i, rem)]

        ans = dfs(0, amount)
        return -1 if ans >= INF else ans
