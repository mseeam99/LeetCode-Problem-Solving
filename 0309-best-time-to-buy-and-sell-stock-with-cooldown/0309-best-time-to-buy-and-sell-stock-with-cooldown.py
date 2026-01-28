class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        memo = {}

        def recursion(index,allowedToBuy,waiting):

            if (index >= len(prices)):
                return 0

            if (index,allowedToBuy,waiting) in memo:
                return memo[(index,allowedToBuy,waiting)]
            
            if allowedToBuy == True:
                pick = -prices[index] + recursion(index+1,False,False)
                notPick = 0 + recursion(index+1,True,False)
                profit = max(pick,notPick)
                memo[(index,allowedToBuy,waiting)] = profit
                return profit
            else:
                pick = prices[index] + recursion(index+2,True,True)
                notPick = 0 + recursion(index+1,False,True)
                profit = max(pick,notPick)
                memo[(index,allowedToBuy,waiting)] = profit
                return profit

        return recursion(0,True,False)        