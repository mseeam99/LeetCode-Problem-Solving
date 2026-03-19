class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:

        hashMap = defaultdict(list)
        for i in range(len(times)):
            u,v,w = times[i][0],times[i][1],times[i][2]
            hashMap[u].append([v,w])

        minHeap = [[0,k]]
        heapq.heapify(minHeap)
        mySet = set()
        maxTime = float("-inf")
        while minHeap:
            time, source = heapq.heappop(minHeap)
            if source in mySet:
                continue
            mySet.add(source)
            maxTime = max(maxTime,time)
            listOfSourceAndTime = hashMap[source]
            for i in range(len(listOfSourceAndTime)):
                if listOfSourceAndTime[i][0] not in mySet:
                    newSource = listOfSourceAndTime[i][0]
                    newTime = listOfSourceAndTime[i][1]
                    newTime += time
                    heapq.heappush(minHeap,[newTime,newSource])    
               

        if len(mySet) == n:
            return maxTime
        else:
            return -1




        