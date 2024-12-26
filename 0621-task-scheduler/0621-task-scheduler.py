class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        keyAndValue = Counter(tasks)
        count = []
        for values in keyAndValue.values():
            count.append(values*-1)
        myQueue = deque()
        currentTime = 0
        heapq.heapify(count)
        while count or myQueue:
            if count:
                workingValue = heapq.heappop(count)
                workingValue = workingValue + 1
                if workingValue != 0:
                    shouldBeAGoodTime = currentTime + n
                    myQueue.append((shouldBeAGoodTime,workingValue))
            if myQueue and myQueue[0][0] == currentTime:
                mostLeftGoodTime, mostLeftValue = myQueue.popleft()
                heapq.heappush(count,mostLeftValue)
            currentTime+=1
        return currentTime



            
            






        