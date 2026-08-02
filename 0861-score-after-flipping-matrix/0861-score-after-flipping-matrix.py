class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:

        for r in range(len(grid)):
            currentRow = grid[r]
            #need to change
            if currentRow[0] == 0:
                for c in range(len(grid[r])):
                    grid[r][c] = grid[r][c] ^ 1

        for c in range(len(grid[0])):
            theColumnList = []
            for r in range(len(grid)):
                theColumnList.append(grid[r][c])
            oneCount = theColumnList.count(1)
            zeroCount = theColumnList.count(0)
            if zeroCount > oneCount:
                for v in range(len(theColumnList)):
                    theColumnList[v] = theColumnList[v] ^ 1
            for r in range(len(grid)):
                grid[r][c] = theColumnList[r]
        
        val = 0
        for i in range(len(grid)):
            currentRow = grid[i][::-1]
            for j in range(len(currentRow)):
                if currentRow[j] != 0:
                    val += 2**j

        return val