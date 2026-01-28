class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:

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