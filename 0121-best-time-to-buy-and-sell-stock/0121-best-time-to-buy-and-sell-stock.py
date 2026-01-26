class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        previousLowestValue = prices[0]
        maxProfit = 0
        for i in range(1,len(prices)):
            currentDayValue = prices[i]
            maxProfit = max(maxProfit,(currentDayValue-previousLowestValue))
            previousLowestValue = min(previousLowestValue,prices[i])
        return maxProfit

