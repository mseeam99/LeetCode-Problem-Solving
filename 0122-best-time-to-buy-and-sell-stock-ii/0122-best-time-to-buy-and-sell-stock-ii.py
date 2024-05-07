class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        leftPointer = 0
        rightPointer = leftPointer + 1
        while rightPointer < len(prices):
            if prices[leftPointer] <= prices[rightPointer]:
                tempDifference = prices[rightPointer] - prices[leftPointer]
                profit += tempDifference
                leftPointer += 1
                rightPointer = leftPointer + 1
            elif prices[leftPointer] > prices[rightPointer]:
                leftPointer += 1
                rightPointer = leftPointer + 1
        return profit