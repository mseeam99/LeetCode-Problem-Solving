class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = []
        for i in range(len(prices)+1):
            tempArray = [0]*(2)
            dp.append(tempArray)
        dp[len(prices)][0] = dp[len(prices)][1] = 0
        for index in range(len(prices)-1,-1,-1):
            for canBuy in range(0,2):
                if canBuy == 1:
                    pick = -prices[index] + dp[index+1][0]
                    notPick = 0 + dp[index+1][1]
                    result = max(pick,notPick)
                    dp[index][canBuy] = result
                else:
                    pick = prices[index] + dp[index+1][1]
                    notPick = 0 + dp[index+1][0]
                    result = max(pick,notPick)
                    dp[index][canBuy] = result
        return min(dp[0])
        '''
        def recursion(index,canBuy):

            if index >= len(prices):
                return 0

            if dp[index][canBuy] != 0:
                return dp[index][canBuy]

            if canBuy == 1:
                pick = -prices[index] + recursion(index+1,0)
                notPick = 0 + recursion(index+1,1)
                result = max(pick,notPick)
                dp[index][canBuy] = result
                return result
            else:
                pick = prices[index] + recursion(index+1,1)
                notPick = 0 + recursion(index+1,0)
                result = max(pick,notPick)
                dp[index][canBuy] = result
                return result
                
        return recursion(0,1)
        '''