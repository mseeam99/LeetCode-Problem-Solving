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

        for c in range(len(matrix[0])):
            eachColumnSum = 0
            for r in range(len(matrix)):
                eachColumnSum += matrix[r][c]
            
            r = 0
            while eachColumnSum > colSum[c]:
                difference = eachColumnSum-colSum[c]
                maxShift = min(matrix[r][c],difference)
                matrix[r][c] -= maxShift
                matrix[r][c+1] += maxShift
                eachColumnSum -= maxShift
                r += 1
                
        
        return matrix






                
        
                    



