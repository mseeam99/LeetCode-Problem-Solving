class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        totalAnswer = [[0] * len(matrix)  for _ in range(len(matrix[0]))]
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                totalAnswer[j][i] = matrix[i][j]
        return totalAnswer
        