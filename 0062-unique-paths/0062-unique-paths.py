class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        '''        
        memo = {}
        def recursion(row,col):

            if row == 0 and col == 0:
                return 1

            if row < 0 or col < 0:
                return 0
            
            if (row,col) in memo:
                return memo[row,col]
        
            left = recursion(row,col-1)
            up   = recursion(row-1,col)
            memo[(row,col)] = left+up
            return left+up

        return recursion(m-1,n-1)
        '''
        '''
        dp = []
        for i in range(m):
            tempDp = [0]*n
            dp.append(tempDp)

        def recursion(row,col):
            if dp[row][col] != 0:
                return dp[row][col]

            if row < 0 or col < 0:
                return 0

            if row == 0 and col == 0:
                return 1

            left = recursion(row,col-1)
            up   = recursion(row-1,col)

            dp[row][col] = left+up
            return left+up
        
        ans = recursion(m-1,n-1)

        for i in range(len(dp)):
            print(dp[i])

        return ans
        '''



        dp = []
        for i in range(m):
            tempDp = [0]*n
            dp.append(tempDp)

        for i in range(len(dp)):
            for j in range(len(dp[i])):
                if i == 0 or j == 0:
                    dp[i][j] = 1
                else:
                    dp[i][j] = 0

        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0:
                    continue
                else:
                    dp[i][j] = dp[i][j-1] + dp[i-1][j]

        return dp[m-1][n-1]







        


