class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo = {}
        def recursion(index,alreadyBoughtOne):
            if index >= len(prices):
                return 0
            if (index,alreadyBoughtOne) in memo:
                return memo[(index,alreadyBoughtOne)]
            buy, sell, skip = 0,0,0
            if alreadyBoughtOne == False:
                buy = recursion(index+1,True) - prices[index]
                skip = recursion(index+1,False)
                memo[(index,alreadyBoughtOne)] = max(buy,skip)
            if alreadyBoughtOne == True:
                sell = recursion(index+1,False) + prices[index]
                skip = recursion(index+1,True)
                memo[(index,alreadyBoughtOne)] = max(sell,skip)
            return memo[(index,alreadyBoughtOne)]
        return recursion(0,False)