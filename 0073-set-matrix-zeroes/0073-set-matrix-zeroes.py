class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        
        firstRow    = None
        firstColumn = None
        
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 0:
                    if i == 0: firstRow    = True
                    if j == 0: firstColumn = True
                    matrix[0][j] = 0
                    matrix[i][0] = 0
        
        for i in range(1,len(matrix)):
            for j in range(1,len(matrix[i])):
                if matrix[0][j] == 0 or matrix[i][0] == 0:
                    matrix[i][j] = 0
                    
        #row
        if firstRow == True:
            for i in range(len(matrix[0])):
                matrix[0][i] = 0
        #column
        if firstColumn == True:
            for i in range(len(matrix)):
                matrix[i][0] = 0
               






