class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:

        answerCount = 0
        visitedSet = set()

        def function(r,c):
            if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]):
                return False

            if grid[r][c] == 1:
                return True
            if (r,c) in visitedSet:
                return True

            visitedSet.add((r,c))
            

            right = function(r,c+1)
            down  = function(r+1,c)
            left  = function(r,c-1)
            up    = function(r-1,c)

            if right == False or down == False or left == False or up == False:
                return False

            if right == True and down == True and left == True and up == True:
                return True
            

    


        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if (i,j) not in visitedSet:
                    if grid[i][j] == 0:
                        ans = function(i,j)
                        if ans == True:
                            answerCount+=1

        return answerCount



        