class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        price = 0
        leftPointer = 0
        rightPointer = leftPointer + 1
        while rightPointer < len(prices):
            if prices[leftPointer] <= prices[rightPointer]:
                tempProfit = prices[rightPointer] - prices[leftPointer]
                price = max(price,tempProfit)
                rightPointer += 1
            elif prices[leftPointer] > prices[rightPointer]:
                leftPointer +=1
                rightPointer = leftPointer + 1
        return price



        
        