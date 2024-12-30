class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        for i in range(len(trips)):
            trips[i] = (trips[i][1], trips[i][2], trips[i][0])
        
        trips.sort()
        
        alreadyInCarQueue = []
        heapq.heapify(alreadyInCarQueue)
        
        for bigTripFrom, bigTripTo, bigTripPerson in trips:
            while alreadyInCarQueue and alreadyInCarQueue[0][0] <= bigTripFrom:
                _, _, currentTripPerson = heapq.heappop(alreadyInCarQueue)
                capacity += currentTripPerson 
            
            if bigTripPerson > capacity:
                return False
            
            capacity -= bigTripPerson
            heapq.heappush(alreadyInCarQueue, (bigTripTo, bigTripFrom, bigTripPerson))
        
        return True