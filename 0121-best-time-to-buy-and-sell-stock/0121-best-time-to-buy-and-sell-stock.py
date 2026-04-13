class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minimum = prices[0]
        profit = 0
        for i in range(len(prices)):
            profit = max(profit,(prices[i]-minimum))
            minimum = min(minimum,prices[i])
        return profit









        