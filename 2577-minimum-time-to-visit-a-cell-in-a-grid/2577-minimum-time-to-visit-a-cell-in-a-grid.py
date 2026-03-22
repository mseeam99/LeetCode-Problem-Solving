class Solution:
    def minimumTime(self, grid: List[List[int]]) -> int:

        if grid[0][1] > 1 and grid[1][0] > 1:
            return -1

        minHeap = [[0,0,0]] # time,row,col
        heapq.heapify(minHeap)
        visitedSet = set()
        directions = [[0,1],[1,0],[0,-1],[-1,0]]
        
        while minHeap:

            time, row, col = heapq.heappop(minHeap)

            if (row, col) in visitedSet:
                continue
            visitedSet.add((row, col))
            
            if row == len(grid)-1 and col == len(grid[0])-1:
                return time

            for i in range(len(directions)):
                newRow, newCol = directions[i][0]+row, directions[i][1]+col
                if newRow < 0 or newRow >= len(grid) or newCol < 0 or newCol >= len(grid[0]):
                    continue
                if (newRow, newCol) in visitedSet:
                    continue

                arrival_time = time + 1

                if arrival_time >= grid[newRow][newCol]:
                    wait_time = 0
                else:
                    wait_time = grid[newRow][newCol] - arrival_time

                # parity fix
                if wait_time % 2 == 1:
                    wait_time += 1

                nextTime = arrival_time + wait_time
                            
                heapq.heappush(minHeap, [nextTime, newRow, newCol])

            
        return -1
            

                
                



            

            
            
            
            










        