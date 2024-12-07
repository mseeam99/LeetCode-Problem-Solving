class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:

        oneDimensionalList = []

        for i in range(len(mat)):
            for j in range(len(mat[i])):
                oneDimensionalList.append(mat[i][j])

        if r * c != len(oneDimensionalList):
            return mat

        newMatrix = []
        for i in range(r):
            newList = []
            for j in range(c):
                newList.append("")
            newMatrix.append(newList)

        n = 0
        for i in range(len(newMatrix)):
            for j in range(len(newMatrix[i])):
                newMatrix[i][j] = oneDimensionalList[n]
                n += 1

        return newMatrix
                
        

        



        