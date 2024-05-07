class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        profit = 0
        left  = 0
        right = left + 1

        while right < len(prices):
            if prices[right] < prices[left]:
                left  += 1
                right = left + 1
            elif prices[right] >= prices[left]:
                tempDifference = prices[right] - prices[left]
                profit = max(profit,tempDifference)
                right+=1

        return profit
        