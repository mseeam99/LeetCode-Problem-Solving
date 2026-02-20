class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        dp = [[0] * n for _ in range(m)]

        for i in range(len(dp)):
            for j in range(len(dp[i])):
                if i == 0 or j == 0:
                    dp[i][j] = matrix[i][j]
                else:
                    dp[i][j] = 0

        for i in range(1,len(dp)):
            for j in range(1,len(dp[i])):
                if matrix[i][j] == 0:
                    continue
                else:
                    dp[i][j] = min(dp[i-1][j],dp[i-1][j-1],dp[i][j-1]) + matrix[i][j]

        answer = 0
        for i in range(len(dp)):
            for j in range(len(dp[i])):
                answer+=dp[i][j]
        return answer

            

        