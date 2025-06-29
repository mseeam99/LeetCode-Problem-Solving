class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        first  = float("inf")
        second = float("inf")
        indexTrack = 0
        for i in range(len(prices)):
            if prices[i] < first:
                first = prices[i]
                indexTrack = i
        for i in range(len(prices)):
            if prices[i] >= first and i != indexTrack:
                second = min(second,prices[i])
        print(first)
        print(second)
        totalCost = (first+second)
        leftOver = money-(totalCost)
        if leftOver >= 0:
            return leftOver
        return money
        