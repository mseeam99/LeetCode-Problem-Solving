class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        positionOne = -1
        positionTwo = -1
        answer = float("inf")
        for i in range(len(wordsDict)):
            word = wordsDict[i]
            if word == word1:
                positionOne = i
            elif word == word2:
                positionTwo = i
            if positionOne != -1 and positionTwo != -1:
                difference = abs(positionTwo-positionOne)
                answer = min(answer,difference)
        return answer