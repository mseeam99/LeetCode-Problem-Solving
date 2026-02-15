class Solution:
    def generatePossibleNextMoves(self, currentState: str) -> List[str]:

        answerList = []

        for i in range(len(currentState)-1):
            if currentState[i] == "+" and currentState[i+1] == "+":

                leftPart   = currentState[:i]
                curentPart = "--"
                rightPart  = currentState[i+2:]

                string = leftPart + curentPart + rightPart
                answerList.append(string)

        return answerList
            