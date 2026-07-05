class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        hashMap = defaultdict(list)
        for i in range(len(roads)):
            currentMap = roads[i]
            start = currentMap[0]
            end = currentMap[1]
            hashMap[start].append(end)
            hashMap[end].append(start)
        assignedList = []
        for key,val in hashMap.items():
            length = len(val)
            theTuple = (-length,key,val)
            assignedList.append(theTuple)
        heapq.heapify(assignedList)
        assignedHashMap = {}
        while assignedList:
            theTuple = heapq.heappop(assignedList)
            length,nodeNumber,connectionList = -theTuple[0], theTuple[1], theTuple[2]
            assignedHashMap[nodeNumber] = n
            n-=1
        total = 0
        for i in range(len(roads)):
            currentMap = roads[i]
            start = currentMap[0]
            end = currentMap[1]
            total += assignedHashMap[start]
            total += assignedHashMap[end]
        return total
















        