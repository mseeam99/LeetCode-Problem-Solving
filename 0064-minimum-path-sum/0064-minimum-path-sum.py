class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        '''
        memo = {}
        def recursion(row,col):
            nonlocal memo
            if row < 0 or col < 0:
                return float("inf")
            if row == 0 and col == 0:
                return grid[row][col]
            if (row,col) in memo:
                return memo[(row,col)]
            up   = grid[row][col] + recursion(row-1,col)
            left = grid[row][col] + recursion(row,col-1)
            memo[(row,col)] = min(up,left)
            return memo[(row,col)]
        return recursion(len(grid)-1,len(grid[0])-1)
        '''
        
        '''
        #Tabulation
        dp = []
        for i in range(len(grid)):
            currentRow = [0] * len(grid[i])
            dp.append(currentRow)

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if i == 0 and j == 0:
                    dp[i][j] = grid[i][j]
                    continue
                if i-1 < 0:
                    upMax = float("inf")
                else:
                    upMax = dp[i-1][j]
                if j-1 < 0:
                    leftMax = float("inf")
                else:
                    leftMax = dp[i][j-1]
                up   = grid[i][j] + upMax
                left = grid[i][j] + leftMax
                dp[i][j] = min(up,left)
        return dp[len(dp)-1][len(dp[0])-1]
        '''
        
        #Tabulation
        prev = grid[0]
        for i in range(1,len(prev)):
            prev[i] += prev[i-1]
        for i in range(1,len(grid)):
            temp = [0] * len(grid[i])
            for j in range(len(grid[i])):
                if j == 0:
                    temp[j] = grid[i][j] + prev[j]
                    continue
                up   = grid[i][j] + prev[j]
                left = grid[i][j] + temp[j-1]
                temp[j] = min(up,left)
            prev = temp
        return prev[-1]





                
                
               

                    




        

        




        





        
       

            

            
            




            
        