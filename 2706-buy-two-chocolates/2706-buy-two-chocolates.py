class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        heapq.heapify(prices)
        firstMin = heapq.heappop(prices)
        secotMin = heapq.heappop(prices)
        val = money - (firstMin + secotMin)
        if val < 0:
            return money
        return val