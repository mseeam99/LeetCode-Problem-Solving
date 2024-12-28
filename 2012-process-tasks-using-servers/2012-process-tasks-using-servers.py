class Solution:
    def assignTasks(self, servers: List[int], tasks: List[int]) -> List[int]:

        for i in range(len(servers)):
            servers[i] = (servers[i],i)
        heapq.heapify(servers)
        
        currentTime = 0
        serverQueue = []
        answer = []

        for i in range(len(tasks)):

            currentTime = max(currentTime, i)  

            if not servers:
                currentTime = serverQueue[0][0]

            if serverQueue:
                while serverQueue and serverQueue[0][0] <= currentTime:
                    availableTime, weight, index = heapq.heappop(serverQueue)
                    heapq.heappush(servers, (weight, index))
                    
            if servers:
                taskTime = tasks[i]
                weight, index = heapq.heappop(servers)
                answer.append(index)
                heapq.heappush(serverQueue, (currentTime + taskTime, weight, index))

        return answer