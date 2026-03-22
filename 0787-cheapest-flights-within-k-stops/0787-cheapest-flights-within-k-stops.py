class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:

        hashMap = defaultdict(list)
        for i in range(len(flights)):
            start, stop, price = flights[i][0],flights[i][1],flights[i][2]
            hashMap[start].append([stop,price])
            # start -> stop, price

        print(hashMap)

        minHeap = [[0,0,src]] # cost, increm, stop
        heapq.heapify(minHeap)
        visitedSet = set()
        minPriceNeeded = float("-inf")
       
       

        while minHeap:

            cost, stopIncrement, stop = heapq.heappop(minHeap)


            if stop == dst and stopIncrement - 1 <= k:
                return cost
            
            if (stop,cost) in visitedSet or stopIncrement > k:
                continue
            visitedSet.add((stop,cost))

            arrayOfDirections = list(hashMap[stop])
            for i in range(len(arrayOfDirections)):
                
                newStop, newCost = arrayOfDirections[i][0],arrayOfDirections[i][1]+cost
                newStopIncrement = stopIncrement + 1


                heapq.heappush(minHeap,[newCost,newStopIncrement,newStop])

        return -1





            

            



            





        


        