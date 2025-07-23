class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        
        dp = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if i == j:
                    dp[i][j] = grid[m-1][i]
                else:
                    dp[i][j] = grid[m-1][i] + grid[m-1][j]

        for row in range(m-2, -1, -1):
            new_dp = [[0] * n for _ in range(n)]
            for i in range(n):
                for j in range(n):
                    max_val = 0
                    for di in [-1, 0, 1]:
                        for dj in [-1, 0, 1]:
                            ni, nj = i + di, j + dj
                            if 0 <= ni < n and 0 <= nj < n:
                                val = dp[ni][nj]
                                if i == j:
                                    val += grid[row][i]
                                else:
                                    val += grid[row][i] + grid[row][j]
                                max_val = max(max_val, val)
                    new_dp[i][j] = max_val
            dp = new_dp 

        return dp[0][n-1]
