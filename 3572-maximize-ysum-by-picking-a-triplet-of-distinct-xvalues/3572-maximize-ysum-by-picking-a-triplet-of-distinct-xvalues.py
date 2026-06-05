class Solution:
    def maxSumDistinctTriplet(self, x: List[int], y: List[int]) -> int:

        for i in range(len(y)):
            y[i] = (-y[i],x[i])

        heapq.heapify(y)

        seen = set()
        iteration = 0
        maxSum = 0

        while len(y):

            realValueToSum, setCheckValue = heapq.heappop(y)
            realValueToSum = -realValueToSum

            if setCheckValue not in seen:
                seen.add(setCheckValue)
                maxSum += realValueToSum
                iteration += 1
            
            if iteration == 3:
                return maxSum
                
    
        return -1