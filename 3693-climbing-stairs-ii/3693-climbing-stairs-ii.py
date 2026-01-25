class Solution:
    def climbStairs(self, n: int, costs: List[int]) -> int:

        dp = [float('inf')] * (n + 1)
        dp[0] = 0

        for i in range(0, n):
            for k in (1, 2, 3):
                
                if i+k <= n:
                    dp[i+k] = min(dp[i+k], dp[i] + (costs[i + k   - 1] + k * k))

        return dp[n]