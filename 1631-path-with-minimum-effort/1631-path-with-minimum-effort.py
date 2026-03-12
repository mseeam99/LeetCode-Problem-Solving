class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        minHeap = [[0,0,0]]
        heapq.heapify(minHeap)
        visitedSet = set()
        directions = [[0,1],[1,0],[0,-1],[-1,0]]
        while minHeap:
            currArray = heapq.heappop(minHeap)
            diff, row, col = currArray[0], currArray[1], currArray[2]
            if (row,col) in visitedSet:
                continue
            visitedSet.add((row,col))
            if row == len(heights)-1 and col == len(heights[0])-1:
                return diff
            for i in range(len(directions)):
                newRow, newCol = row + directions[i][0], col + directions[i][1]
                if (newRow < 0 or newRow > len(heights)-1) or (newCol < 0 or newCol > len(heights[0])-1) or (newRow,newCol) in visitedSet:
                    continue
                newDiff = max(diff, abs(heights[newRow][newCol]-heights[row][col]))
                heapq.heappush(minHeap,[newDiff,newRow,newCol])