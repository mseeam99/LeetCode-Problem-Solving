class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = []
        for i in range(len(prices)+2):
            secondDimension = [0]*(2)
            dp.append(secondDimension)
                    
        #index -> i
        #allowedToBuy -> j

        for i in range(len(prices)-1,-1,-1):

            for j in range(2):

                if j == 1:
                    pick = -prices[i] + dp[i+1][0]
                    notPick = 0 + dp[i+1][1]
                    dp[i][j] = max(pick,notPick)
                   
                else:
                    pick = (prices[i] + dp[i+2][1])
                    notPick = (0 + dp[i+1][0])
                    dp[i][j] = max(pick,notPick)

        
        for i in range(len(dp)):

            print(dp[i])

        return dp[0][1]



               


'''

        def recursion(index,allowedToBuy,waiting):

            if (index >= len(prices)):
                return 0
            
            if dp[index][allowedToBuy][waiting] != 0:
                return dp[index][allowedToBuy][waiting]
            
            if allowedToBuy == 1:
                pick = -prices[index] + recursion(index+1,0,1)
                notPick = 0 + recursion(index+1,1,1)
                profit = max(pick,notPick)
                dp[index][allowedToBuy][waiting] = profit
                return profit
            else:
                pick = prices[index] + recursion(index+2,1,0)
                notPick = 0 + recursion(index+1,0,0)
                profit = max(pick,notPick)
                dp[index][allowedToBuy][waiting] = profit
                return profit

        return recursion(0,1,1)       
'''