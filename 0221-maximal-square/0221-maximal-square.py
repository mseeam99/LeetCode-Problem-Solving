from typing import List

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if len(matrix) == 1 and len(matrix[0]) == 1:
            return int(matrix[0][0])

        rows, cols = len(matrix), len(matrix[0])

        # Preprocess: count consecutive '1's to the right
        for row in range(rows - 1, -1, -1):
            for col in range(cols - 1, -1, -1):
                if matrix[row][col] != '0':
                    if col < cols - 1:
                        matrix[row][col] = int(matrix[row][col]) + int(matrix[row][col + 1])
                    else:
                        matrix[row][col] = int(matrix[row][col])
                else:
                    matrix[row][col] = 0

        maxSquareSize = 0

        # Check for maximal square
        for i in range(rows):
            for j in range(cols):
                currentWidth = matrix[i][j]
                if currentWidth == 0:
                    continue

                minWidth = currentWidth
                for k in range(i, i + currentWidth):
                    if k >= rows:
                        break
                    minWidth = min(minWidth, matrix[k][j])
                    if minWidth < (k - i + 1):
                        break
                    maxSquareSize = max(maxSquareSize, k - i + 1)

        return maxSquareSize * maxSquareSize
