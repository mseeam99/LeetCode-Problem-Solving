class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        memo = {}

        def recursion(index,holding):
            if index >= len(prices):
                return 0

            if (index,holding) in memo:
                return memo[(index,holding)]

            if holding == False:
                buy = -prices[index] + recursion(index+1,True)
                skip = recursion(index+1,False)
                memo[(index,holding)] = max(buy, skip)
            elif holding == True:
                sell = prices[index]
                skip = recursion(index+1,True)

                memo[(index,holding)] = max(sell, skip)

            return memo[(index,holding)]

        return recursion(0,False)
            
        