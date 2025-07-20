class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:

        outerArray = [0] * len(grid[0])     

        for row in range(len(grid)-1,-1,-1):

            currentRow = grid[row]

            for col in range(len(grid[0])-1,-1,-1):

                if col == len(grid[0])-1 and row == len(grid)-1:
                    continue
                elif col == len(grid[0])-1:
                    currentRow[col] += outerArray[col] 
                    continue
                elif row == len(grid)-1:
                    currentRow[col] += currentRow[col+1]
                    continue

                rightValue = 0
                downValue = 0

                if col+1 <= len(currentRow)-1:
                    rightValue = currentRow[col+1]
                if col <= len(outerArray)-1:
                    downValue = outerArray[col]

                minimumNeigbour = min(rightValue,downValue)

                currentRow[col] += minimumNeigbour 
            
            outerArray = currentRow
        
        return outerArray[0]

