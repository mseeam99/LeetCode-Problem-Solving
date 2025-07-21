class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:

        outerArray = [0] * len(matrix[0])

        for row in range(len(matrix)-1,-1,-1):

            innerCurrentArray = matrix[row]

            for col in range(len(matrix[0])-1,-1,-1):

                rightDiagonal, down, leftDiagonal = float("inf"),float("inf"),float("inf")

                if col+1 <= len(matrix[0])-1:
                    rightDiagonal = outerArray[col+1]

                down = outerArray[col]

                if col-1 >= 0:
                    leftDiagonal = outerArray[col-1]

                innerCurrentArray[col] += min(rightDiagonal, down, leftDiagonal)

            outerArray = innerCurrentArray

        return(min(outerArray))

            



        