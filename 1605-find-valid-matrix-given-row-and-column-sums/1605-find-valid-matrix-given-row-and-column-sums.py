class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:

        matrix = []
        for i in range(len(rowSum)):
            row = [0]*len(colSum)
            matrix.append(row)

        for r in range(len(matrix)):
            for c in range(len(matrix[r])):
                if c == 0:
                    matrix[r][c] = rowSum[r]

        for c in range(len(colSum) - 1):      
            eachColumnSum = 0
            for r in range(len(rowSum)):
                eachColumnSum += matrix[r][c] 
            r = 0
            while eachColumnSum > colSum[c] and r < len(rowSum):
                difference = eachColumnSum - colSum[c]
                shift = min(matrix[r][c], difference)
                matrix[r][c] -= shift
                matrix[r][c + 1] += shift
                eachColumnSum -= shift
                r += 1

        return matrix