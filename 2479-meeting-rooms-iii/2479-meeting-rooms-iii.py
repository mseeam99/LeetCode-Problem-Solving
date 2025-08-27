class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        
        if n == 0:
            return 0

        meetings.sort()
        hashMap = {}

        availableRoomsArray = []
        for i in range(n):
            availableRoomsArray.append(i)
        currentlyUsingRoomsArray = []
        heapq.heapify(availableRoomsArray)
        heapq.heapify(currentlyUsingRoomsArray)


        for i in range(len(meetings)):

            startTime = meetings[i][0]
            endTime = meetings[i][1]

            # can use a room which finished before or just before interval starts
            while currentlyUsingRoomsArray and currentlyUsingRoomsArray[0][0] <= startTime:
                finishingTime, roomNumber = heapq.heappop(currentlyUsingRoomsArray)
                heapq.heappush(availableRoomsArray,roomNumber)
                
            if availableRoomsArray:
                roomNumber = heapq.heappop(availableRoomsArray)
                heapq.heappush(currentlyUsingRoomsArray,(endTime,roomNumber))
                if roomNumber not in hashMap:
                    hashMap[roomNumber] = 1
                else:
                    hashMap[roomNumber] += 1
            else:
                # meeting will be dalayed and pop the first available room and use it, current end time + delay
                finishingTime, roomNumber = heapq.heappop(currentlyUsingRoomsArray)
                duration = endTime - startTime
                willEndAt = finishingTime + duration
                heapq.heappush(currentlyUsingRoomsArray, (willEndAt, roomNumber))

                if roomNumber not in hashMap:
                    hashMap[roomNumber] = 1
                else:
                    hashMap[roomNumber] += 1

        maxRoomNumber = float("-inf")
        maxValue = float("-inf")
        for key,val in hashMap.items():
            if val > maxValue:
                maxValue = val
                maxRoomNumber = key

        return maxRoomNumber
                    

            
