class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:

        minHeap = [[0,0,0]]
        heapq.heapify(minHeap)
        visitedSet = set()
        while minHeap:
            effort, row, col = heapq.heappop(minHeap)
            if (row, col) in visitedSet:
                continue
            visitedSet.add((row, col))
            if row == len(heights)-1 and col == len(heights[0])-1:
                return effort
            directions = [[0,1],[1,0],[0,-1],[-1,0]]
            for i in range(len(directions)):
                newRow, newCol = directions[i][0]+row, directions[i][1]+col
                if newRow >= len(heights) or newRow < 0 or newCol >= len(heights[0]) or newCol < 0:
                    continue
                maxEffort = max(abs(heights[newRow][newCol]-heights[row][col]), effort)
                heapq.heappush(minHeap,[maxEffort,newRow,newCol])