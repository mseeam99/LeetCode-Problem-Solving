class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:

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


        





        
       

            

            
            




            
        