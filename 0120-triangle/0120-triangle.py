class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:

        outerRow = [0] * len(triangle[-1])

        for row in range(len(triangle)-1,-1,-1):

            currentRow = triangle[row]

            for col in range(len(triangle[row])-1,-1,-1):

                if row == len(triangle)-1 and col == len(triangle[-1])-1:
                    continue

                elif row == len(triangle)-1:
                    outerRow = currentRow
                    continue

                down_right_diagonal, down = 0,0

                down = outerRow[col]
                down_right_diagonal = outerRow[col+1]
                minimumNeighbour = min(down,down_right_diagonal)
                currentRow[col] += minimumNeighbour

            outerRow = currentRow

        return outerRow[0]