class Solution:
    def climbStairs(self, n: int, costs: List[int]) -> int:

        dp = [float('inf')] * (n+1)
        dp[0] = 0

        for i in range(n+1):

            for j in [1,2,3]:

                if i+j <= n:
                    dp[i + j] = min(dp[i+j], (dp[i] + costs[ i + j - 1] + ((i+j-i)**2)))

        return dp[-1]





       