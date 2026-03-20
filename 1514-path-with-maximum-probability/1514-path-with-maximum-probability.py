class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        
        hashMap = defaultdict(list)
        for i in range(len(edges)):
            start, end, cost = edges[i][0], edges[i][1], succProb[i]
            hashMap[start].append((end, cost))
            hashMap[end].append((start, cost))

        minHeap = [[-1.0,start_node]] 
        visitedSet = set()
        minCost = float("-inf")

        while minHeap:

            cost,end = heapq.heappop(minHeap)
            cost = -cost

            if end in visitedSet:
                continue
            visitedSet.add(end)

            if end == end_node:
                return cost

            
            theList = hashMap[end]
            for i in range(len(theList)):

                if theList[i][0] not in visitedSet:

                    newEnd = theList[i][0]
                    newCost = theList[i][1]*cost

                    heapq.heappush(minHeap,(-newCost,newEnd))
                     

                
        
        return 0.0
        




        