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

        dp = []
        for i in range(m):
            tempDp = [-1]*n
            dp.append(tempDp)

        def recursion(row,col):
            if dp[row][col] != -1:
                return dp[row][col]
            if row == 0 and col == 0:
                return 1
            if row < 0 or col < 0:
                return 0
            left = recursion(row,col-1)
            up   = recursion(row-1,col)
            dp[row][col] = left+up
            return left+up

        return recursion(m-1,n-1)