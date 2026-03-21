class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:

        minHeap = [[0,0,0]]
        heapq.heapify(minHeap)
        visitedSet = set()
        minObstacke = float("-inf")

        while minHeap:
            cost, row, col = heapq.heappop(minHeap)
            if (row, col) in visitedSet:
                continue
            visitedSet.add((row,col))

            if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]):
                continue

            minObstacke = max(minObstacke,cost)
            if row == len(grid)-1 and col == len(grid[0])-1:
                return minObstacke

            directions = [[0,1],[1,0],[0,-1],[-1,0]]

            for i in range(len(directions)):

                newRow, newCol = directions[i][0]+row, directions[i][1]+col
                if (newRow, newCol) in visitedSet:
                    continue
                if newRow < 0 or newRow >= len(grid) or newCol < 0 or newCol >= len(grid[0]):
                    continue

                newCost = grid[newRow][newCol] + cost
                heapq.heappush(minHeap,[newCost, newRow, newCol])
        

        return minObstacke
                
                

            
            






        