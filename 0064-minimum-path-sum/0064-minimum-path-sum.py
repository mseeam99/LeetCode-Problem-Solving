class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:

        memo = {}

        def recursion(row,col):
            nonlocal memo

            if row < 0 or col < 0 or row >= len(grid) or col >= len(grid[0]):
                return float("inf")

            if row == len(grid)-1 and col == len(grid[0])-1:
                return grid[row][col]
            
            if (row,col) in memo:
                return memo[(row,col)]

            right =  grid[row][col] + recursion(row,col+1)
            down  =  grid[row][col] + recursion(row+1,col)
            memo[(row,col)] = min(right,down)
            return min(right,down)
        
        return recursion(0,0)
       

            

            
            




            
        