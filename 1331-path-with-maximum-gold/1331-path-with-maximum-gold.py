class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:

        visitedSet = set()

        def function(r,c):
          
            if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]) or (r,c) in visitedSet or grid[r][c] == 0:
                return 0

            visitedSet.add((r,c))

            gold = grid[r][c]

            right = function(r,c+1)
            down  = function(r+1,c)
            left  = function(r,c-1)
            up    = function(r-1,c)

            visitedSet.remove((r,c))

            return gold + max(right,down,left,up)

        maxValue = 0

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] != 0:
                    eachIterReturn = function(r,c)
                    maxValue = max(maxValue,eachIterReturn)
                     
        return maxValue
        