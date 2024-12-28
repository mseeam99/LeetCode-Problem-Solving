class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                grid[i][j] = grid[i][j] * -1

        answer = 0
        totalLength = len(grid)
        smallArrayLength = len(grid[0])

        smallIdx = 0

        while smallIdx < smallArrayLength:
            singlePassMaxValue = 0
            for i in range(totalLength):
                heapq.heapify(grid[i])
                biggestValueAsNegative = heapq.heappop(grid[i])
                biggestValueAsNegative = biggestValueAsNegative * -1
                singlePassMaxValue = max(singlePassMaxValue,biggestValueAsNegative)
                
            answer += singlePassMaxValue
            smallIdx+=1

        return answer



        