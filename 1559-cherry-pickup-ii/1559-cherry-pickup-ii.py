class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = [[[0] * n for _ in range(n)] for _ in range(m)]

        for i in range(n):
            for j in range(n):
                if i == j:
                    dp[m-1][i][j] = grid[m-1][i]
                else:
                    dp[m-1][i][j] = grid[m-1][i] + grid[m-1][j]

        for row in range(m-2, -1, -1):
            for i in range(n):
                for j in range(n):
                    maxValue = 0
                    for moveForI in range(-1, 2):
                        for moveForJ in range(-1, 2):
                            newI = i + moveForI
                            newJ = j + moveForJ
                            if 0 <= newI < n and 0 <= newJ < n:
                                value = dp[row+1][newI][newJ]
                                if i == j:
                                    value += grid[row][i]
                                else:
                                    value += grid[row][i] + grid[row][j]
                                maxValue = max(maxValue, value)
                    dp[row][i][j] = maxValue

        return dp[0][0][n-1]
