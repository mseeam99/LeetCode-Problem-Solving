class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:

        setOfBoundary = set()

        def function(r,c):

            if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]):
                return False

            if (r,c) in setOfBoundary:
                return True

            if grid[r][c] == 0:
                return False

            setOfBoundary.add((r,c))

            function(r,c+1)
            function(r+1,c)
            function(r,c-1)
            function(r-1,c)

            return False
            

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    if i == 0 or i == len(grid)-1 or j == 0 or j == len(grid[0])-1:
                        function(i,j)

        setOfEverything = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    setOfEverything.add((i,j))

        return len(setOfEverything) - len(setOfBoundary)
        

        

        




        