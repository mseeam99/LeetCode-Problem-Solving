class Solution:
    def climbStairs(self, n: int, costs: List[int]) -> int:

        dp = [float('inf')] * (n + 1)
        dp[0] = 0

        for i in range(0, n):              
            for k in (1, 2, 3):            
                j = i + k                 
                if j <= n:
                    dp[j] = min(dp[j], dp[i] + (costs[j - 1] + k * k))

        return dp[n]


        