class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minimumValue = prices[0]
        maxProfit = float("-inf")
        for i in range(len(prices)):
            minimumValue = min(minimumValue,prices[i])
            maxProfit = max(maxProfit,prices[i]-minimumValue)
        return maxProfit


        

        