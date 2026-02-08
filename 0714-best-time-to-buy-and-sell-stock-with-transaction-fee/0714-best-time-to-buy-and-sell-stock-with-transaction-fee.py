class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        
        memo = {}

        def recursion(index,canBuy):
            if (index >= len(prices)):
                return 0
            
            if (index,canBuy) in memo:
                return memo[(index,canBuy)]

            if canBuy == True:
                pick = -prices[index] + recursion(index+1,False)
                notPick = 0 + recursion(index+1,True)
                maxProfit = max(pick,notPick)
                memo[(index,canBuy)] = maxProfit
                return maxProfit
            else:
                pick = (prices[index]-fee) + recursion(index+1,True)
                notPick = 0 + recursion(index+1,False)
                maxProfit = max(pick,notPick)
                memo[(index,canBuy)] = maxProfit
                return maxProfit

        return recursion(0,True)