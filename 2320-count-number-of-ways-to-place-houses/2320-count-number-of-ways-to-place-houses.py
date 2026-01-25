class Solution:
    def countHousePlacements(self, n: int) -> int:

       

        modVal = (10**9) + 7

        dp = [0] * (n+1)
        dp[0] = 1
        dp[1] = 2
        
        

        for i in range(2,n+1):
            
            if i-1 >= 0:
                lastValue = dp[i-1]
            else:
                lastValue = 0
            
            if i-2 >= 0:
                veryLeftValue = dp[i-2]
            else:
                veryLeftValue = 0

            dp[i] = (lastValue + veryLeftValue) % modVal


        total = (dp[n] * dp[n]) % modVal

        
        return total











        