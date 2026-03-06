class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:

        hashMap = {}
        for i in range(len(times)):
            u,v,w = times[i]
            if u not in hashMap:
                hashMap[u] = []
            hashMap[u].append([v, w])

        time = 0
        minHeap = [(0,k)]
        visitedSet = set()

        while minHeap:
            weight1, node1 = heapq.heappop(minHeap)
            if node1 in visitedSet:
                continue
            visitedSet.add(node1)
            time = max(time,weight1)
            if node1 in hashMap:
                theArray = hashMap[node1]
                for i in range(len(theArray)):
                    node2, weight2 = theArray[i][0], theArray[i][1]
                    if node2 not in visitedSet:
                        heapq.heappush(minHeap,(weight1+weight2,node2))
            
        if len(visitedSet) == n:
            return time
        else:
            return -1




















        return time
        
    
       
        