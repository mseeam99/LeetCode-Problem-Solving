class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        firstRow  = set("qwertyuiop")
        secondRow = set("asdfghjkl")
        thirdRow  = set("zxcvbnm")
        answer = []
        for i in range(len(words)):
            tempWord = set(words[i].lower())
            if (tempWord <= firstRow) or (tempWord <= secondRow) or (tempWord <= thirdRow):
                answer.append(words[i])
        return answer