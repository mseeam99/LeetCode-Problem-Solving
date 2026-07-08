class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:

        arrivalTime = []
        for i in range(len(dist)):
            arrival = ceil(dist[i] / speed[i])
            arrivalTime.append(arrival)

        heapq.heapify(arrivalTime)
        currTimeAsMinuite = 0
        totalElimination = 0

        while arrivalTime:
            monsterComingAt = heapq.heappop(arrivalTime)
            if currTimeAsMinuite >= monsterComingAt:
                return totalElimination

            currTimeAsMinuite += 1
            totalElimination += 1

        return totalElimination 

        
        