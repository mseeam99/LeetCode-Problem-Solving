class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        MOD = 10**9 + 7

        hashMap = defaultdict(list)
        for i in range(len(roads)):
            source, destination, time = roads[i][0],roads[i][1],roads[i][2]
            hashMap[source].append([time,destination])
            hashMap[destination].append([time,source])
        
        minHeap = [[0,0]] #time, destination
        heapq.heapify(minHeap)
        mini_time = [float("inf")] * n
        path_cont = [0] * n
        mini_time[0] = 0
        path_cont[0] = 1

        while minHeap:

            time, destination = heapq.heappop(minHeap)

            for i in range(len(hashMap[destination])):

                newTime, newDestination = hashMap[destination][i][0]+time,hashMap[destination][i][1]

                if newTime < mini_time[newDestination]:

                    mini_time[newDestination] = newTime
                    path_cont[newDestination] = path_cont[destination] % MOD
                    heapq.heappush(minHeap,[newTime, newDestination])
                
                elif newTime == mini_time[newDestination]:
                    path_cont[newDestination] = (path_cont[destination] + path_cont[newDestination]) % MOD

        return path_cont[n-1]



        