class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:

        rowLength = len(obstacleGrid)
        colLength = len(obstacleGrid[0])

        previousArrayDP = [0] * colLength

        for row in range(rowLength):

            currentArrayDP = [0] * colLength

            for col in range(colLength):

                if row >= 0 and col >= 0 and obstacleGrid[row][col] == 1:
                    currentArrayDP[col] = 0

                elif row < 0 or col < 0:
                    currentArrayDP[col] = 0

                elif row == 0 and col == 0:
                    currentArrayDP[col] = 1

                else:
                    currentArrayDP[col] = previousArrayDP[col] + currentArrayDP[col-1]

            previousArrayDP = currentArrayDP

        return previousArrayDP[-1]







      