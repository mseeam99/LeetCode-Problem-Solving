class Solution:
    def countHousePlacements(self, n: int) -> int:

        modVal = (10**9) + 7

        dp = [0] * (n+1)
        dp[0] = 1
        dp[1] = 2
        
        

        for i in range(2,n+1):
            
            lastValue = dp[i-1]
            veryLeftValue = dp[i-2]
            dp[i] = (lastValue + veryLeftValue) % modVal

        total = (dp[-1] * dp[-1]) % modVal

        
        return total











        