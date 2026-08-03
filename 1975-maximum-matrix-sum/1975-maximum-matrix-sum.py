class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:

        totalSum = 0
        negativeCount = 0
        smallestValue = float("inf")

        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                totalSum += abs(matrix[i][j])
                smallestValue = abs(min(smallestValue,abs(matrix[i][j])))
                if matrix[i][j] < 0:
                    negativeCount += 1

        if negativeCount % 2 == 1:
            totalSum -= 2*smallestValue

        return totalSum

                
                

        