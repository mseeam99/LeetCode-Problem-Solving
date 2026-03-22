class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        minHeap = [[0,0,0]]
        heapq.heapify(minHeap)
        visitedSet = set()
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        while minHeap:
            cost,row,col = heapq.heappop(minHeap)
            if (row,col) in visitedSet:
                continue
            visitedSet.add((row,col))
            if row == len(grid)-1 and col == len(grid[0])-1:
                return cost
            if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]):
                continue
            for i in range(len(directions)):
                rowIdx, colIdx = directions[i][0],directions[i][1]
                newRow, newCol = row + rowIdx, col + colIdx
                if (newRow < 0 or newRow >= len(grid) or newCol < 0 or newCol >= len(grid[0])):
                    continue
                if ((newRow,newCol) in visitedSet):
                    continue
                if grid[row][col] == i + 1:
                    newCost = cost
                else:
                    newCost = cost + 1
                heapq.heappush(minHeap,[newCost,newRow,newCol])
        return -1

                

               
                







            

            



            
        