class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        dp = []
        for i in range(len(prices)+1):
            tempArray = [0]*(2+1)
            dp.append(tempArray)

        for i in range(len(prices)-1,-1,-1):
            for j in range(2):
                if j == 1: # buying
                    pick = -prices[i] + dp[i+1][0]
                    notPick = 0 + dp[i+1][1]
                    dp[i][j] = max(pick,notPick)
                elif j == 0: # selling
                    pick = (+prices[i] + dp[i+1][1]) - fee
                    notPick = 0 + dp[i+1][0]
                    dp[i][j] =  max(pick,notPick)
        return dp[0][1]
'''
        def recursion(index,ifAllowedToBuy):

            if index >= len(prices):
                return 0

            if ifAllowedToBuy == 1: # buying
               
                pick = -prices[index] + recursion(index+1,0)
                notPick = 0 + recursion(index+1,1)
                return max(pick,notPick)
                

            elif ifAllowedToBuy == 0: # selling
                pick = (+prices[index] + recursion(index+1,1)) - fee
                notPick = 0 + recursion(index+1,0)
                return max(pick,notPick)

            
            
        return recursion(0,1)



'''