class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        previousLowestValue = prices[0]
        maxProfitTotal = 0
        profit = 0
        for i in range(1,len(prices)):
            currentDayValue = prices[i]
            profit = currentDayValue-previousLowestValue
            if profit > 0:
                maxProfitTotal += profit
                previousLowestValue = prices[i]
                continue
            previousLowestValue = min(previousLowestValue,prices[i])
        return maxProfitTotal


        