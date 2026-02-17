class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:

        newArray = matrix[:]
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                newArray[i][j] = int(matrix[i][j])
                
        for i in range(len(newArray)):
            for j in range(len(newArray[0])):
                if i == 0 or j == 0:
                    continue
                else:
                    top      = newArray[i-1][j]
                    diagonal = newArray[i-1][j-1]
                    left     = newArray[i][j-1]
                    if newArray[i][j] == 0:
                        continue
                    if top == diagonal == left:
                        newArray[i][j] = 1 + top 
                    else:
                        newArray[i][j] = 1 + min(top,diagonal,left)

        maxValue = 0
        for i in range(len(newArray)):
            for j in range(len(newArray[i])):
                maxValue = max(maxValue,newArray[i][j])
        return maxValue ** 2
          