class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        memo = {}
        def recurison(row,col1,col2):
            nonlocal memo
            if (row,col1,col2) in memo:
                return memo[(row,col1,col2)]
            if row < 0 or row >= len(grid) or col1 < 0 or col1 >= len(grid[0]) or col2 < 0 or col2 >= len(grid[0]):
                return 0
            maxVal = float("-inf")
            for i in [-1,0,1]:
                for j in [-1,0,1]:
                    value = 0
                    if col1 == col2:
                        value = grid[row][col1]                
                    else:
                        value = grid[row][col1] + grid[row][col2]
                    value += recurison(row+1,col1+i,col2+j)
                    maxVal = max(maxVal,value)
            memo[(row,col1,col2)] = maxVal
            return maxVal
        return recurison(0,0,len(grid[0])-1)
        