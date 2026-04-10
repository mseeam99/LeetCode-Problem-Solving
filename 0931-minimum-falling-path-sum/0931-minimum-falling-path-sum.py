class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:

        prev = [0] * len(matrix[0])

        for i in range(len(matrix)):

            temp = [0] * len(matrix[i])

            for j in range(len(matrix[i])):

                if i >= 0 and i <= len(matrix)-1 and j-1 >= 0 and j-1 <= len(matrix[0])-1:
                    upLeft     = matrix[i][j] + prev[j-1]
                else:
                    upLeft = float("inf")

                if i >= 0 and i <= len(matrix)-1 and j >= 0 and j <= len(matrix[0])-1:
                    upStraight = matrix[i][j] + prev[j]
                else:
                    upStraight = float("inf")

                if i >= 0 and i <= len(matrix)-1 and j+1 >= 0 and j+1 <= len(matrix[0])-1:
                    upRight    = matrix[i][j] + prev[j+1]
                else:
                    upRight = float("inf")

                minValue = min(upLeft,upStraight,upRight)
                temp[j] = minValue

            prev = temp
            
        return min(prev)





        