class NumMatrix:

    def __init__(self, matrix: list[list[int]]):

        self.newMatrix = []
        for i in range(len(matrix)):
            newLinearArray = [0] * len(matrix[i])
            self.newMatrix.append(newLinearArray)

        self.newMatrix[0][0] = matrix[0][0]

        for r in range(1,len(self.newMatrix)):
            self.newMatrix[r][0] = self.newMatrix[r-1][0] + matrix[r][0]
        
        for c in range(1,len(self.newMatrix[0])):
            self.newMatrix[0][c] = matrix[0][c] + self.newMatrix[0][c-1]

        for row in range(1,len(self.newMatrix)):
            for col in range(1,len(self.newMatrix[0])):
                self.newMatrix[row][col] = matrix[row][col] + self.newMatrix[row-1][col] + self.newMatrix[row][col-1] - self.newMatrix[row-1][col-1]

        #for i in range(len(self.newMatrix)):
        #    print(self.newMatrix[i])

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:

        totalSum = 0
        upperValue = 0
        leftValue = 0
        addAgain = 0

        totalSum = self.newMatrix[row2][col2] 
        if row1-1 >= 0:
            upperValue = self.newMatrix[row1-1][col2] 
        else:
            upperValue = 0
        if col1-1 >= 0:
            leftValue = self.newMatrix[row2][col1-1]
        else:
            leftValue = 0
        if row1-1 >= 0 and col1-1 >= 0:
            addAgain = self.newMatrix[row1-1][col1-1]
        else:
            addAgain = 0
        return totalSum - (upperValue + leftValue) + addAgain

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)