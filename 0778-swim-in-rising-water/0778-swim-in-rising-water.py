class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        minHeap = [[grid[0][0],0,0]] #time,row,col
        heapq.heapify(minHeap)
        visitedSet = set()
        minTime = float("-inf")
        while minHeap:
            time, row, col = heapq.heappop(minHeap)
            if (row,col) in visitedSet:
                continue
            visitedSet.add((row,col))
            if row < 0 and row > len(grid)-1 and col < 0 and col > len(grid[0])-1:
                continue
            minTime = max(minTime,time)
            if row == len(grid)-1 and col == len(grid[0])-1:
                return minTime
            directions = [[0,1],[1,0],[0,-1],[-1,0]]
            for i in range(len(directions)):
                rowIdx, colIdx = row + directions[i][0], col + directions[i][1]
                if (rowIdx, colIdx) in visitedSet:
                    continue
                if rowIdx >= 0 and rowIdx <= len(grid)-1 and colIdx >= 0 and colIdx <= len(grid[0])-1:
                    heapq.heappush(minHeap,[grid[rowIdx][colIdx],rowIdx,colIdx])
        return minTime

                




        