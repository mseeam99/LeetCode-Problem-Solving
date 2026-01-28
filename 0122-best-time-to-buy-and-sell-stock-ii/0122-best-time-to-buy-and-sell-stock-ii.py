class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        memo = {}
        
        def recursion(index,canBuy):

            if index >= len(prices):
                return 0

            if (index,canBuy) in memo:
                return memo[(index,canBuy)]
            
            if canBuy == True:
                pick = -prices[index] + recursion(index+1,False)
                notPick = 0 + recursion(index+1,True)
                result = max(pick,notPick)
                memo[(index,canBuy)] = result
                return result
            else:
                pick = prices[index] + recursion(index+1,True)
                notPick = 0 + recursion(index+1,False)
                result = max(pick,notPick)
                memo[(index,canBuy)] = result
                return result
                
        return recursion(0,True)