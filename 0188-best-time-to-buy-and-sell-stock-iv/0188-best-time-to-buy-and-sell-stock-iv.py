class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:

        dp = []
        for i in range(len(prices)+1):
            SecondDimension = []
            for j in range(2):
                thirdDimension = []
                for k in range(k+1):
                    thirdDimension.append(0)
                SecondDimension.append(thirdDimension)
            dp.append(SecondDimension)

        for index in range(len(prices)-1,-1,-1):
            for ifBuyingPossible in range(2):
                for capacity in range(1,k+1):
                    if ifBuyingPossible == 1:
                        pick = -prices[index] + dp[index+1][0][capacity]
                        notPick = 0 + dp[index+1][1][capacity]
                        result = max(pick,notPick)
                        dp[index][ifBuyingPossible][capacity] = result
                    elif ifBuyingPossible == 0:
                        pick = prices[index] + dp[index+1][1][capacity-1]
                        notPick = 0 + dp[index+1][0][capacity]
                        result = max(pick,notPick)
                        dp[index][ifBuyingPossible][capacity] = result
        return dp[0][1][k]   


        '''
        memo = {}
        
        def recursion(index,canBuy,allowed):
            if (index >= len(prices)) or (allowed <= 0):
                return 0

            if (index,canBuy,allowed) in memo:
                return memo[(index,canBuy,allowed)]

            if canBuy == True:
                pick = -prices[index] + recursion(index+1,False,allowed)
                notPick = 0 + recursion(index+1,True,allowed)
                profit = max(pick,notPick)
                memo[(index,canBuy,allowed)] = profit
                return profit
            else:
                pick = prices[index] + recursion(index+1,True,allowed-1)
                notPick = 0 + recursion(index+1,False,allowed)
                profit = max(pick,notPick)
                memo[(index,canBuy,allowed)] = profit
                return profit
            
        return recursion(0,True,k)  
        '''