class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        hashMap = {}
        for i in range(len(times)):
            u,v,w = times[i]
            if u not in hashMap:
                hashMap[u] = []
            hashMap[u].append([w,v])

        time = 0
        minHeap = [(0,k)]
        mySet = set()
        while minHeap:
            weight1, node1 = heapq.heappop(minHeap)
            if node1 in mySet:
                continue
            mySet.add(node1)
            time = max(time,weight1)
            if node1 in hashMap:
                theList = hashMap[node1]
                for i in range(len(theList)):
                    weight2, node2 = theList[i]
                    heapq.heappush(minHeap,(weight1+weight2,node2))
        
        if len(mySet) == n:
            return time
        else:
            return -1