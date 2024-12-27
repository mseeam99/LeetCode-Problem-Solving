class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        
        for i in range(len(tasks)):
            tasks[i].append(i)
            newValueAsTuple = (tasks[i][0],tasks[i][1],tasks[i][2])
            tasks[i] = newValueAsTuple

        tasks.sort()

        answerList = []
        minHeap = []  
        idx = 0
        cpuAvailableAt = tasks[0][0]  

        while idx < len(tasks) or len(minHeap) != 0:
            while idx < len(tasks) and tasks[idx][0] <= cpuAvailableAt:
                enqueueTime, processingTime, index = tasks[idx]
                heapq.heappush(minHeap, (processingTime, index))
                idx += 1

            if len(minHeap) != 0:
                processingTime, index = heapq.heappop(minHeap)
                cpuAvailableAt += processingTime
                answerList.append(index)
            else:
                cpuAvailableAt = tasks[idx][0]

        return answerList
