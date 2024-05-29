class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        leftPointer  = 0
        rightPointer = leftPointer + 1

        profit = 0

        while rightPointer < len(prices):
            if prices[rightPointer] > prices[leftPointer]:
                tempDifference = prices[rightPointer] - prices[leftPointer]
                profit += tempDifference
                leftPointer += 1
                rightPointer = leftPointer + 1 
            elif prices[rightPointer] <= prices[leftPointer]:
                leftPointer += 1
                rightPointer = leftPointer + 1 
            
        return profit



        
        