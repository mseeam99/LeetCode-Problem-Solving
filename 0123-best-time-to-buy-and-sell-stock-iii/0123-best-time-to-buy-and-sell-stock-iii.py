class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        memo = {}

        def recursion(index, ifBuyingPossible, capacity):

            if (index,ifBuyingPossible,capacity) in memo:
                return memo[(index,ifBuyingPossible,capacity)]

            if (index >= len(prices)) or (capacity <= 0):
                return 0

            if ifBuyingPossible == True:
                x = -prices[index] + recursion(index+1,False,capacity)
                y = 0 + recursion(index+1,True,capacity)
                result = max(x,y)
                memo[(index,ifBuyingPossible,capacity)] = result
                return result

            elif ifBuyingPossible == False:
                x = prices[index] + recursion(index+1,True,capacity-1)
                y = 0 + recursion(index+1,False,capacity)
                result = max(x,y)
                memo[(index,ifBuyingPossible,capacity)] = result
                return result


        return recursion(0,True,2)
        




        