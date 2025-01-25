class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        count = 0
        visitedStart = set()

        def backTrack(r,c):

            if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]) or grid[r][c] == "0" or (r,c) in visitedStart:
                return 
            visitedStart.add((r,c))
            backTrack(r,c+1)  
            backTrack(r+1,c) 
            backTrack(r,c-1) 
            backTrack(r-1,c)
            
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i,j) not in visitedStart and grid[i][j] == "1":
                    backTrack(i,j)
                    count+=1

        return count



        