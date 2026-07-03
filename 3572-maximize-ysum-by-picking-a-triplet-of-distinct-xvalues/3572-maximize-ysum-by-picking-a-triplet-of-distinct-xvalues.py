class Solution:
    def maxSumDistinctTriplet(self, x: List[int], y: List[int]) -> int:

        heap = []
        for i in range(len(y)):
            tempTuple = (-y[i],x[i])
            heap.append(tempTuple)

        heapq.heapify(heap)
        

        seenIndex = set()
        summation = []
        
        while heap:

            yVal, xVal = heapq.heappop(heap)
            yVal = yVal * -1

            if xVal not in seenIndex:
                seenIndex.add(xVal)
                summation.append(yVal)
            else:
                continue

            if len(summation) == 3:
                break
        
        if len(summation) == 3:
            return sum(summation)
        else:
            return -1






            