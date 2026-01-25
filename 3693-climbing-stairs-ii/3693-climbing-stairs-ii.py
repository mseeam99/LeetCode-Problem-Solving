class Solution:
    def climbStairs(self, n: int, costs: List[int]) -> int:

        dp = [float('inf')] * (n + 1)
        dp[0] = 0

        for i in range((n+1)):

            for j in [1,2,3]:
                prevStep = i - j
                if prevStep >= 0 and prevStep <= len(costs)-1:
                    cost = costs[i-1] + ((j)**2)
                
                    dp[i] = min(dp[i],(dp[prevStep]+cost))
            
        return dp[-1]




        