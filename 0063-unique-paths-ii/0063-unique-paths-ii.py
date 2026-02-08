class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:

        if obstacleGrid[len(obstacleGrid)-1][len(obstacleGrid[0])-1] == 1:
            return 0

        memo = {}

        def recursion(row,col):

            if (row < 0 or col < 0 or row >= len(obstacleGrid) or col >= len(obstacleGrid[0])):
                return 0
            
            if (row == len(obstacleGrid)-1) and (col == len(obstacleGrid[0])-1):
                return 1
            
            if obstacleGrid[row][col] == 1:
                return 0
            
            if (row,col) in memo:
                return memo[(row,col)]

            right = recursion(row,col+1)
            down  = recursion(row+1,col)

            totalWays = right + down

            memo[(row,col)] = totalWays

            return totalWays


        return recursion(0,0)

            
            
        