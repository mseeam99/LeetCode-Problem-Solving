class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:

        hashMap = defaultdict(list)
        for i in range(len(edges)):
            start,end,weight = edges[i][0],edges[i][1],edges[i][2]
            hashMap[start].append([weight,end])
            hashMap[end].append([weight,start])
            # start -> [[weight,end]]
        
        #print(hashMap)

        answer = []
        for i in range(n):
            answer.append(set())

        def function(it):
            minHeap = [[0,it]] # weight, end
            heapq.heapify(minHeap)
            visitedSet = set()

            while minHeap:

                weight,end = heapq.heappop(minHeap)

                if end in visitedSet or weight > distanceThreshold:
                    continue
                visitedSet.add(end)


                theList = hashMap[end]
                for i in range(len(theList)):
                    newWeight, newEnd = theList[i][0]+weight,theList[i][1]
                    if newWeight <= distanceThreshold:
                        if it != newEnd:
                            answer[it].add(newEnd)
                    heapq.heappush(minHeap,[newWeight, newEnd])
        
        

        for it in range(n):
            function(it)

        
        print(answer)
        minIdx = 0
        minLength = float("inf")
        for i in range(len(answer)):
            if len(answer[i]) <= minLength:
                minLength = len(answer[i])
                minIdx = i
        return minIdx





                









        