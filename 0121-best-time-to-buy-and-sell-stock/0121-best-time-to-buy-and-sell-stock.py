class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minStock = float("inf")
        maxProfit = 0
        for i in range(len(prices)):
            maxProfit = max(maxProfit,(prices[i]-minStock))
            minStock = min(minStock,prices[i])
        return maxProfit

            
