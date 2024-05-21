class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        answer = [[1]]
        for i in range(1,numRows):
            tempAnswer = []
            tempRow = [0] + answer[-1] + [0]
            for j in range(len(answer[-1])+1):
                tempAnswer.append(tempRow[j]+tempRow[j+1])
            answer.append(tempAnswer)
        return answer